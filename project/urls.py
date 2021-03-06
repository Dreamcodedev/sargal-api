from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop.views import CategoryAPIView, ProductAPIView, UserAPIView, CommandAPIView, UserCreateAPIView, UserUpdateAPIView,TripAPIView,TripCreateAPIView,CommandCreateAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
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

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
