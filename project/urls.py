from django.contrib import admin
from django.urls import path, include
from shop.views import CategoryAPIView, ProductAPIView, ArticleAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/categroy/', CategoryAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/product/', ProductAPIView.as_view({'get': 'list',
        'post':'create'})),
    path('api/article/', ArticleAPIView.as_view({'get': 'list',
        'post':'create'}))
]
