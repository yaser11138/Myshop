from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import homepage, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path("shop/", include("shop.urls")),
    path("", homepage, name="home"),
    path("about/", about, name="about"),
    path("cart/", include("cart.urls")),
    path("order/", include("order.urls")),
    path("zibal/", include("zibal.urls")),
    path("coupon/", include("coupon.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
