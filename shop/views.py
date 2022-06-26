from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shop.models import Category, Product, Article, User, Command
from shop.serializers import CategorySerializer, ProductSerializer, ArticleSerializer, UserSerializer, CommandSerializer

class CategoryAPIView(ModelViewSet):


    serializer_class = CategorySerializer
    queryset = Category.objects.all()
            


class ProductAPIView(ModelViewSet):


    serializer_class = ProductSerializer
    #queryset = Product.objects.all()

    def get_queryset(self):
    # Nous récupérons tous les produits dans une variable nommée queryset
        queryset = Product.objects.filter(active=True)
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset



class ArticleAPIView(ModelViewSet):
    serializer_class = ArticleSerializer
    #queryset = Article.objects.all()
    def get_queryset(self):
    # Nous récupérons tous les produits dans une variable nommée queryset
        queryset = Article.objects.filter(active=True)
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        product_id = self.request.GET.get('product_id')
        if product_id is not None:
            queryset = queryset.filter(product_id=product_id)
        return queryset




class UserAPIView(ModelViewSet):


    serializer_class = UserSerializer
    queryset = User.objects.all()
            


class CommandAPIView(ModelViewSet):


    serializer_class = CommandSerializer
    #queryset = Product.objects.all()

    def get_queryset(self):
    # Nous récupérons tous les produits dans une variable nommée queryset
        queryset = Command.objects.filter(active=True)
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        command_id = self.request.GET.get('command_id')
        if command_id is not None:
            queryset = queryset.filter(command_id=command_id)
        return queryset