from django.conf import settings
from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.SESSION_CART_ID)
        if not cart:
            cart = self.session[settings.SESSION_CART_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        print("before", self.cart)
        if product_id not in self.cart:
            print(1)
            self.cart[product_id] = {"quantity": quantity, "price": product.price}
        if override_quantity:
            print(2)
            self.cart[product_id]["quantity"] = quantity
        else:
            print(3)
            self.cart[product_id]["quantity"] += quantity
            print("after", self.cart)
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
        return sum(item["quantity"] * item["price"] for item in self.cart.values())

    def clear(self):
        self.session.pop("cart")
        self.save()

    def save(self):
        self.session.modified = True
