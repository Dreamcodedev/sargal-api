from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shop.models import Category, Product, Article
from shop.serializers import CategorySerializer, ProductSerializer, ArticleSerializer

class CategoryAPIView(ModelViewSet):


    serializer_class = CategorySerializer
    queryset = Category.objects.all()



            


class ProductAPIView(ModelViewSet):


    serializer_class = ProductSerializer
    queryset = Product.objects.all()



class ArticleAPIView(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


