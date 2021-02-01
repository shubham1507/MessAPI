from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
# router.register(r'', SubscriptionViewSet)
# router.register(r'customer/subscription', CustomerViewSet)

router.register('Service', views.Service, base_name='Service') #Service Url added

urlpatterns = [

    path('', include(router.urls)),
    path('custsub/<slug:sub_id>/',views.CustomerSubscriptionView.as_view(),name='custsub')
]

