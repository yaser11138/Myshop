from io import BytesIO
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import weasyprint
from django.conf import settings
from order.models import Order


@shared_task
def invoice_sender(order_id):
    order = Order.objects.get(id=order_id)
    subject = f"My Shop Order {order_id} invoice"
    message = "Thank you for Shopping"
    email = EmailMessage(subject, message, "admin@admin.com", [order.email])
    invoice = BytesIO()
    pdf_template = render_to_string("order/pdf/order_bill_pdf.html", {"order": order})
    weasyprint.HTML(string=pdf_template).write_pdf(invoice, stylesheets=[weasyprint.CSS(
        settings.STATIC_FILES + "css/pdf.css"
    )])
    email.attach((f"order_{order_id}", invoice.getvalue(), 'application/pdf'))
    email.send()
    return email
