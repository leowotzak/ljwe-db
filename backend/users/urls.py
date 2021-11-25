from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(
    r"users",  # ! SymbolViewSet
)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
