from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token 
from shop.views import (CategoryAPIView, CodeAPIView, CodeCreateAPIView, 
                        ProductAPIView, UserAPIView, CommandAPIView, UserCreateAPIView, 
                        UserUpdateAPIView,TripAPIView,TripCreateAPIView,CommandCreateAPIView, 
                        PaiementAPIView, PaiementCreateAPIView,home)


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api-auth/', include('rest_framework.urls')),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/category/', CategoryAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/product/', ProductAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/user/', UserAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/user/create', UserCreateAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/user/update', UserUpdateAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/command/', CommandAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/command/create', CommandCreateAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/trip/', TripAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/trip/create', TripCreateAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/code/create', CodeCreateAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/code/', CodeAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/paiement/', PaiementAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/paiement/create', PaiementCreateAPIView.as_view({'get': 'list',
        'post':'create'})),

    path('home', home, name='home'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
