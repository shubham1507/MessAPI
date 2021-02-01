
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework import routers
from .views import UserViewSet,VendorListing
router = routers.DefaultRouter()
router.register('registration', UserViewSet)
router.register('VendorListing', VendorListing,base_name='VendorListing')


urlpatterns = [

    path('', include(router.urls)),
    path('forgot/',views.ForgotPassword.as_view()),
    
    path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='auth_change_password'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
