from django.urls import path, include
from .models import Symbol, BarDataDaily
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class BarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BarDataDaily
        fields = ["timestamp", "open_price", "high_price", "low_price", "close_price"]


class QuerySerializer(serializers.HyperlinkedModelSerializer):

    # bardatadaily_set = BarSerializer(many=True)

    class Meta:
        model = Symbol
        fields = ["symbol_id", "ticker", "name", "description", "sector", "asset_type"]


class SymbolViewSet(viewsets.ModelViewSet):
    queryset = Symbol.objects.using("SecuritiesMaster")
    serializer_class = QuerySerializer

    def list(self, request):
        # x = request.query_params
        # y = QuerySerializer(self.queryset.all())
        x = QuerySerializer(self.queryset.all(), many=True)
        return Response(x.data)


router = routers.DefaultRouter()
router.register(r"symbol", SymbolViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
