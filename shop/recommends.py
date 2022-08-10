import redis as rediserver
from django.conf import settings
from .models import Product

redis = rediserver.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


class Recommender(object):
    def get_product_key(self, id):
        return f"product:{id}:bought_with"

    def product_boughts(self,products):
        product_ids = [product.id for product in products]
        for product_id in product_ids:
            for product_buy_with_id in product_ids:
                if product_id != product_buy_with_id:
                    redis.zincrby(self.get_product_key(product_id),1,product_buy_with_id)

    def suggest_products(self,products,max_result=6):
        product_ids = [product.id for product in products]
        suggestions = []
        if len(product_ids) == 1:
            suggestions = redis.zrange(self.get_product_key(product_ids[0]),0,-1,desc=True)[:max_result]
        elif  len(product_ids) > 1:
            flat_ids = ''.join([str(id) for id in product_ids])
            flat_ids_key = f"flat_id_{flat_ids}"
            prodcut_keys = [self.get_product_key(id) for id in product_ids]
            redis.zunionstore(flat_ids_key,prodcut_keys)
            redis.zrem(flat_ids_key, *product_ids)
            suggestions = redis.zrange(flat_ids_key, 0, -1, desc=True)[:max_result]
            redis.delete(flat_ids_key)     
        suggestions_products = [Product.objects.get(id=int(id)) for id in suggestions]
        return suggestions_products
    