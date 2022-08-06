from django.conf import settings
from shop.models import Product
from coupon.models import Coupon


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.coupon_id = self.session.get("coupon-id", None)
        cart = self.session.get(settings.SESSION_CART_ID)
        if not cart:
            cart = self.session[settings.SESSION_CART_ID] = {}
        self.cart = cart

    @property
    def coupon(self):
        try:
            return Coupon.objects.get(id=self.coupon_id)
        except:
            return None

    def add(self, product, quantity, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": quantity, "price": product.price}
        elif override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def delete(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        prodcuts = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in prodcuts:
            cart[str(product.id)]["product"] = product
        for item in cart.values():
            item["total_price"] = item["quantity"] * item["price"]
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        total_price = sum(item["quantity"] * item["price"] for item in self.cart.values())
        return round(total_price, 2)

    def get_discount(self):
        if self.coupon:
            discount = (self.coupon.discount / 100) * self.get_total_price()
            return round(discount, 2)
        else:
            return 0

    def get_discounted_price(self):
        discounted_price = self.get_total_price() - self.get_discount()
        return round(discounted_price, 2)

    def clear(self):
        self.session.pop("cart")
        self.save()

    def save(self):
        self.session.modified = True
