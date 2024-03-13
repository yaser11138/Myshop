from io import BytesIO
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import weasyprint
from django.conf import settings
from order.models import Order
from weasyprint.text.fonts import FontConfiguration


@shared_task
def invoice_sender(order_id):
    order = Order.objects.get(id=order_id)
    font_config = FontConfiguration()
    subject = f"My Shop Order {order_id} invoice"
    message = "Thank you for Shopping"
    from_email = "admin@admin.com"
    email = EmailMessage(subject=subject, body=message, from_email=from_email, to=[order.email])
    invoice = BytesIO()
    pdf_template = render_to_string("order/pdf/order_bill_pdf.html", {"order": order})
    weasyprint.HTML(string=pdf_template).write_pdf(invoice, stylesheets=[weasyprint.CSS(
        settings.STATIC_FILES + "css/pdf.css"
    )], font_config=font_config)

    email.attach(f"order_{order_id}", invoice.getvalue(), 'application/pdf')
    email.send()
    return email
