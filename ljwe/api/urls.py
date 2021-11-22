

from django.urls import path, include
from .models import Symbol
from rest_framework import routers, serializers, viewsets

class QuerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Symbol
        fields = ['symbol_id', 'ticker']

class SymbolViewSet(viewsets.ModelViewSet):
    queryset = Symbol.objects.all()
    serializer_class = QuerySerializer

router = routers.DefaultRouter()
router.register(r'symbol', SymbolViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]


