from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token 
from shop.views import (CategoryAPIView, CodeAPIView, CodeCreateAPIView, CodeUpdateAPIView, CommandUpdateAPIView, CommandUpdateAcceptedAPIView, CommandUpdateValidateAPIView, DeliveryPayAPIView, 
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
    path('api/user/update/<int:pk>/', UserUpdateAPIView.as_view({'get': 'list',
        'put':'update'})),
    path('api/command/', CommandAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/command/create', CommandCreateAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/command/update', CommandUpdateAPIView.as_view({'get': 'list',
        'put':'update'})),
    path('api/command/update/validate/<int:pk>/', CommandUpdateValidateAPIView.as_view({'get': 'list',
        'put':'update'})),
    path('api/command/update/refused/<int:pk>/', CommandUpdateAcceptedAPIView.as_view({'get': 'list',
        'put':'update'})),
    path('api/trip/', TripAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/trip/create', TripCreateAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/code/create', CodeCreateAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/code/update', CodeUpdateAPIView.as_view({'get': 'list',
        'put':'update'})),
    path('api/code/', CodeAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/paiement/', PaiementAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/paiement/create', PaiementCreateAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/delivery-pay/', DeliveryPayAPIView.as_view({'get': 'list',
        'post':'create'})),

    path('home', home, name='home'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""router = routers.SimpleRouter()
router.register(r'admin/', admin.site.urls, basename='admin')
router.register(r'api-auth/', include('rest_framework.urls'), basename ='api-auth')
router.register(r'token-auth/', obtain_auth_token, basename ='api_token_auth'),
router.register(r'api/category/', CategoryAPIView, basename='category'),
router.register(r'api/product/', ProductAPIView, basename ='product'),
router.register(r'api/user/', UserAPIView, basename='user'),
router.register(r'api/user/create', UserCreateAPIView,basename='user-create'),
router.register(r'api/user/update', UserUpdateAPIView,basename='user-update'),
router.register(r'api/command/', CommandAPIView,basename='command'),
router.register(r'api/command/create', CommandCreateAPIView, basename='command-create'),
router.register(r'api/command/update', CommandUpdateAPIView,basename ='command-update'),
router.register(r'api/command/update/validate/{pk}', CommandUpdateValidateAPIView,basename='command-validate'),
router.register(r'api/command/update/refused', CommandUpdateAcceptedAPIView,basename='command-refused'),
router.register(r'api/trip/', TripAPIView,basename='trip'),
router.register(r'api/trip/create', TripCreateAPIView,basename='trip-create'),
router.register(r'api/code/create', CodeCreateAPIView,basename='code-create'),
router.register(r'api/code/update', CodeUpdateAPIView,basename='code-update'),
router.register(r'api/code/', CodeAPIView,basename='code'),
router.register(r'api/paiement/', PaiementAPIView,basename='paiement'),
router.register(r'api/paiement/create', PaiementCreateAPIView,basename='apiement-create'),
router.register(r'api/delivery-pay/', DeliveryPayAPIView, basename='delivery'),

#router.register(r'home', home, basename ='home'),

urlpatterns = router.urls"""