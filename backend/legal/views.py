from .serializers import CookieSerializer, OffertaSerializer, PolicySerializer
from .models import Cookie, Offerta, Policy
from common.mixins import BaseSectionViewMixin
from drf_spectacular.utils import extend_schema
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


TAG = "Юридическая информация"


@method_decorator(cache_page(60 * 15), name="get")
class OffertaView(BaseSectionViewMixin):
    model = Offerta
    serializer_class = OffertaSerializer

    @extend_schema(tags=[TAG], summary="Оферта")
    def get(self, request):
        return super().get(request)


@method_decorator(cache_page(60 * 15), name="get")
class PolicyView(BaseSectionViewMixin):
    model = Policy
    serializer_class = PolicySerializer

    @extend_schema(tags=[TAG], summary="Политика конфиденциальности")
    def get(self, request):
        return super().get(request)


@method_decorator(cache_page(60 * 15), name="get")
class CookiePolicyView(BaseSectionViewMixin):
    model = Cookie
    serializer_class = CookieSerializer

    @extend_schema(tags=[TAG], summary="Политика cookie")
    def get(self, request):
        return super().get(request)
