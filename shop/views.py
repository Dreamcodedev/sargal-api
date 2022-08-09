from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from shop.models import Category, Product, User, Command, Trip
from shop.serializers import CategorySerializer, ProductSerializer, UserSerializer, CommandSerializer, TripSerializer

@method_decorator(login_required, name='dispatch')
class CategoryAPIView(ModelViewSet):


    serializer_class = CategorySerializer
    queryset = Category.objects.all()
            

@method_decorator(login_required, name='dispatch')
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



"""class ArticleAPIView(ModelViewSet):
    serializer_class = ArticleSerializer
    #queryset = Article.objects.all()
    def get_queryset(self):
    # Nous récupérons tous les produits dans une variable nommée queryset
        queryset = Article.objects.filter(active=True)
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        product_id = self.request.GET.get('product_id')
        if product_id is not None:
            queryset = queryset.filter(product_id=product_id)
        return queryset"""



@method_decorator(login_required, name='dispatch')
class UserAPIView(ModelViewSet):


    serializer_class = UserSerializer
    queryset = User.objects.all()


    #class ProductViewset(ReadOnlyModelViewSet):
 
    #serializer_class = ProductSerializer
 
    def get_queryset(self):
    # Nous récupérons tous les produits dans une variable nommée queryset
        queryset = User.objects.filter(active=True)
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        user_email = self.request.GET.get('email')
        if user_email is not None:
            queryset = queryset.filter(email=user_email)
            #User.objects.get_or_create( email =user_email)


        return queryset

@method_decorator(login_required, name='dispatch')
class UserCreateAPIView(ModelViewSet):


    serializer_class = UserSerializer
    queryset = User.objects.all()

    #class ProductViewset(ReadOnlyModelViewSet):
 
    #serializer_class = ProductSerializer
 
    def get_queryset(self):
        # Nous récupérons tous les produits dans une variable nommée queryset
        #queryset = User.objects.filter(active=True)
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        email = self.request.GET['email']
        firs_name = self.request.GET['firs_name']
        last_name = self.request.GET['last_name']
        phone = self.request.GET['phone']
        address = self.request.GET['address']
        card_money = self.request.GET['card_money']
        active = self.request.GET['active']
        if email is not None:
            #queryset = queryset.filter(email=email)
            #if User.objects.filter(email=email).exists():
            #return
            #else:
            User.objects.get_or_create(email=email,firs_name =firs_name,last_name= last_name, phone= phone,address= address, card_money=card_money, active=active)

            return


        
@method_decorator(login_required, name='dispatch')
class UserUpdateAPIView(ModelViewSet):


    serializer_class = UserSerializer
    queryset = User.objects.all()

    #class ProductViewset(ReadOnlyModelViewSet):
 
    #serializer_class = ProductSerializer
 
    def get_queryset(self):
    # Nous récupérons tous les produits dans une variable nommée queryset
        #queryset = User.objects.filter(active=True)
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        email = self.request.GET['email']
        firs_name = self.request.GET['firs_name']
        last_name = self.request.GET['last_name']
        phone = self.request.GET['phone']
        address = self.request.GET['address']
        active = self.request.GET['active']
        #queryset = queryset.filter(email=user_email)
        if email is not None :
            if User.objects.filter(email=email).exists():
                User.objects.create(email=email, firs_name =firs_name,last_name=last_name,phone=phone,address=address, active=active )

                return

        #update_values = {"firs_name" : firs_name,"last_name": last_name, "phone": phone,"address": address, "active":active}
        #new_values = {"email": email}

        

        

            

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class CommandCreateAPIView(ModelViewSet):


    serializer_class = CommandSerializer
    queryset = Command.objects.all()

    #class ProductViewset(ReadOnlyModelViewSet):
 
    #serializer_class = ProductSerializer
 
    def get_queryset(self):
    # Nous récupérons tous les produits dans une variable nommée queryset
        #queryset = Trip.objects.filter(active=True)
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        email = self.request.GET['email']
        active = self.request.GET['active']
        price = self.request.GET['price']
        quantity = self.request.GET['quantity']
        name = self.request.GET['name']
        if email is not None:
            Command.objects.create( email =email, price=price, quantity=quantity, name=name, active=active)
            return

@method_decorator(login_required, name='dispatch')
class TripAPIView(ModelViewSet):


    serializer_class = TripSerializer
    queryset = Trip.objects.all()


    #class ProductViewset(ReadOnlyModelViewSet):
 
    #serializer_class = ProductSerializer
 
    def get_queryset(self):
    # Nous récupérons tous les produits dans une variable nommée queryset
        queryset = Trip.objects.filter(active=True)
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        trip_email = self.request.GET.get('email')
        if trip_email is not None:
            queryset = queryset.filter(email=trip_email)
            #User.objects.get_or_create( email =user_email)


        return queryset


@method_decorator(login_required, name='dispatch')
class TripCreateAPIView(ModelViewSet):


    serializer_class = TripSerializer
    queryset = Trip.objects.all()

    #class ProductViewset(ReadOnlyModelViewSet):
 
    #serializer_class = ProductSerializer
 
    def get_queryset(self):
    # Nous récupérons tous les produits dans une variable nommée queryset
        #queryset = Trip.objects.filter(active=True)
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        email = self.request.GET['email']
        active = self.request.GET['active']
        departure = self.request.GET['departure']
        arrival = self.request.GET['arrival']
        phone = self.request.GET['phone']
        date_time = self.request.GET['date_time']
        if email is not None:
            Trip.objects.create( email =email, date_time=date_time ,phone=phone, departure=departure, arrival=arrival, active=active)
            return
