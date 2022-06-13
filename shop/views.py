from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shop.models import Category, Product, Article
from shop.serializers import CategorySerializer, ProductSerializer, ArticleSerializer

class CategoryAPIView(APIView):

    def get(self, *args, **kwargs):
        categories=Category.objects.all()
        serializer=CategorySerializer(categories, many=True)

        return Response(serializer.data)


class ProductAPIView(APIView):

    def get(self, *args, **kwargs):
        products=Product.objects.all()
        serializer=ProductSerializer(products, many=True)

        return Response(serializer.data)

class ArticleAPIView(APIView):

    def get(self, *args, **kwargs):
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles, many=True)

        return Response(serializer.data)

