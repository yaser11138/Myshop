from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.template.loader import render_to_string
from cart.cart import Cart
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from .forms import AddOrderform
from .models import OrderItem, Order

font_config = FontConfiguration()


def checkout(request):
    cart = Cart(request)
    if request.method == "POST":
        form = AddOrderform(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = cart.get_discounted_price()
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item["product"], quantity=item["quantity"],
                                         price=item["price"])
            return redirect(reverse("zibal:request", args=[order.id]))
        return render(request, "order/checkout.html", {"form": form})
    else:
        form = AddOrderform()
        return render(request, "order/checkout.html", {"form": form})


@staff_member_required()
def invoice_creator(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    pdf_font_config = FontConfiguration()
    pdf_file = HttpResponse(content_type="appilicatin/pdf")
    pdf_file["Content-Disposition"] = f"filename='order_{order_id}.pdf'"
    pdf_template = render_to_string("order/pdf/order_bill_pdf.html", {"order": order})
    print(order, pdf_template)
    css = CSS(
        settings.STATIC_FILES + "css/pdf.css"
    )
    HTML(string=pdf_template).write_pdf(pdf_file, stylesheets=[css], font_config=pdf_font_config)

    return pdf_file
