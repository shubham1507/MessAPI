from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework import routers
from .views import OrderViewSet
router = routers.DefaultRouter()
router.register(r'', OrderViewSet)


urlpatterns = [

    path('', include(router.urls)),
]

