from django.urls import path, include
from .models import Symbol, BarDataDaily
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class BarSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BarDataDaily
        fields = ['timestamp', 'open_price', 'high_price', 'low_price', 'close_price']


class QuerySerializer(serializers.HyperlinkedModelSerializer):

    bardatadaily_set = BarSerializer(many=True)

    class Meta:
        model = Symbol
        fields = ['symbol_id', 'ticker', 'name', 'description', 'sector', 'asset_type', 'bardatadaily_set']

class SymbolViewSet(viewsets.ModelViewSet):
    # for x in queryset:
    #     y = x.bardatadaily_set.all()
    #     for z in y:
    #         print(dir(z))
    queryset = Symbol.objects.using('SecuritiesMaster').all()
    serializer_class = QuerySerializer

    def list(self, request):

        x = request.query_params
        y = QuerySerializer(self.queryset.select_related())
        print(self.queryset.select_related().first())
        return Response(y.data)


router = routers.DefaultRouter()
router.register(r'symbol', SymbolViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]


