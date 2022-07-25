from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def create_email(order_id):
    order = Order.objects.get(id=order_id)
    subject = f"MyShop Order {order.id} Bill"
    message = f"Thanks so much for your Order! Hope You Enjoy Your New Purchase"
    email = send_mail(subject=subject, message=message, from_email="admin@admin.com",
                      recipient_list=[f"{order.email}"])
    return email
