from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from apps.accounts.views import UserViewSet, VendorListing
from apps.menu.views import MenuListing
from apps.subcriptions.views import Service
# from apps.menu.views import MenuListing
# from apps.accounts.views import UserViewSet
# from apps.subcriptions.views import Service

router = routers.DefaultRouter()

router.register('Service', Service, base_name='Service')
router.register('registration', UserViewSet)
router.register('MenuOfWeek', MenuListing)
router.register('Service', Service)
router.register('MenuOfWeek', MenuListing, base_name='MenuOfWeek')

router.register('VendorListing', VendorListing, base_name='VendorListing')

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include(
        'jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('', include('apps.accounts.urls')),
    path('menu/', include('apps.menu.urls')),
    path('order/', include('apps.orders.urls')),
    path('subscriptions/', include('apps.subcriptions.urls')),
    path('api/gettoken/', TokenObtainPairView.as_view(), name="gettoken"),
    path('api/refresh_token', TokenRefreshView.as_view(),

         name="refresh_token"),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]
