from django.urls import path
from .views import CookieView, OffertaView, PolicyView,


urlpatterns = [
    path("cookie-policy/", CookieView.as_view(), name="cookie-policy"),
    path("offerta/", OffertaView.as_view(), name="offerta"),
    path("policy/", PolicyView.as_view(), name="policy"),
]