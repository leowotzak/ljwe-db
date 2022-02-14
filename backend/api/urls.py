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
        fields = [
            "symbol_id",
            "ticker",
            "name",
            "description",
            "sector",
            "asset_type",
            # "bardatadaily_set",
        ]


class TestSerializer(serializers.HyperlinkedModelSerializer):

    bardatadaily_set = BarSerializer(many=True)

    class Meta:
        model = Symbol
        fields = [
            "symbol_id",
            "ticker",
            "name",
            "description",
            "sector",
            "asset_type",
            "bardatadaily_set",
        ]


class SymbolViewSet(viewsets.ModelViewSet):
    queryset = Symbol.objects
    serializer_class = QuerySerializer

    def list(self, request):
        if not request.query_params:
            x = QuerySerializer(self.queryset.all(), many=True)
            return Response(x.data)

        try:
            id_ = request.query_params["symbol_id"]
        except KeyError:
            raise NotImplementedError
        else:
            print(request.query_params)
            y = TestSerializer(self.queryset.filter(symbol_id=id_), many=True)
            return Response(y.data)


router = routers.DefaultRouter()
router.register(r"symbol", SymbolViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
