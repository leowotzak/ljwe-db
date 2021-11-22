from django.urls import path, include
from .models import Symbol
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

class QuerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Symbol
        fields = ['symbol_id', 'ticker', 'name', 'description', 'sector', 'asset_type']

class SymbolViewSet(viewsets.ModelViewSet):
    queryset = Symbol.objects.using('SecuritiesMaster').all()
    serializer_class = QuerySerializer

router = routers.DefaultRouter()
router.register(r'symbol', SymbolViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]


