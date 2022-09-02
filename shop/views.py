from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, mixins
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from django.core.mail import EmailMultiAlternatives, send_mail


from shop.models import Category, Code, DeliveryPay, Paiement, Product, User, Command, Trip
from shop.serializers import CategorySerializer, CodeSerializer, DeliveryPaySerializer, PaiementSerializer, ProductSerializer, UserSerializer, CommandSerializer, TripSerializer

from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


class CategoryAPIView(ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = CategorySerializer
    queryset = Category.objects.filter(active=True)

class CodeAPIView(ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = CodeSerializer
    queryset = Code.objects.all()

class CodeCreateAPIView(ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = CodeSerializer
    queryset = Code.objects.all()

 
    def get_queryset(self):
        email = self.request.GET['email']
        code = self.request.GET['code']
        amount = self.request.GET['amount']
        recharge = self.request.GET['recharge']
        active = self.request.GET['active']
        if email is not None:
            Code.objects.get_or_create(email=email,code =code,amount= amount, recharge= recharge, active=active)

            return

class CodeUpdateAPIView(ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = CodeSerializer
    queryset = Code.objects.all()
 
    def get_queryset(self):
        active = self.request.GET['active']
        id = self.request.GET['id']
        recharge = self.request.GET['recharge']
        if id is not None :
            code= Code.objects.get(pk=id)
            code.recharge = recharge
            code.save()
            return


class PaiementAPIView(ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = PaiementSerializer
    queryset = Paiement.objects.all()           

class PaiementCreateAPIView(ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = PaiementSerializer
    queryset = Paiement.objects.all()

 
    def get_queryset(self):
        email = self.request.GET['email']
        number = self.request.GET['number']
        delivry = self.request.GET['delivery']
        paiement = self.request.GET['paiement']
        name = self.request.GET['name']
        active = self.request.GET['active']

        if email is not None:
            Paiement.objects.get_or_create(email=email,number =number,delivry= delivry, paiement= paiement, name=name , active=active)

            return



class ProductAPIView(ModelViewSet):

    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = ProductSerializer
    #queryset = Product.objects.all()

    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id) 
        return queryset





class UserAPIView(ModelViewSet):

    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = UserSerializer
    queryset = User.objects.all()
 
    def get_queryset(self):
        queryset = User.objects.filter(active=True)
        user_email = self.request.GET.get('email')
        if user_email is not None:
            queryset = queryset.filter(email=user_email)

        return queryset

class UserCreateAPIView(ModelViewSet):

    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = UserSerializer
    queryset = User.objects.all()
 
    def get_queryset(self):
        email = self.request.GET['email']
        firs_name = self.request.GET['firs_name']
        last_name = self.request.GET['last_name']
        phone = self.request.GET['phone']
        address = self.request.GET['address']
        card_money = self.request.GET['card_money']
        customer = self.request.GET['customer']
        active = self.request.GET['active']
        if email is not None:
            User.objects.get_or_create(email=email,firs_name =firs_name,last_name= last_name, phone= phone,address= address, card_money=card_money, customer=customer, active=active)

            return


        
class UserUpdateAPIView(ModelViewSet):

    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = UserSerializer
    queryset = User.objects.all()
 
    def get_queryset(self):
        email = self.request.GET['email']
        card_money = self.request.GET['card_money']
        active = self.request.GET['active']
        id = self.request.GET['id']
        if email is not None :
            user= User.objects.get(pk=id)
            user.card_money = card_money
            user.save()
            return

        

class CommandAPIView(ModelViewSet):

    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)

    serializer_class = CommandSerializer

    def get_queryset(self):
        queryset = Command.objects.filter(active=True)
        command_id = self.request.GET.get('command_id')
        if command_id is not None:
            queryset = queryset.filter(command_id=command_id)
        return queryset

class CommandCreateAPIView(ModelViewSet):

    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)

    serializer_class = CommandSerializer
    queryset = Command.objects.all()
 
    def get_queryset(self):
        email = self.request.GET['email']
        active = self.request.GET['active']
        price = self.request.GET['price']
        quantity = self.request.GET['quantity']
        name = self.request.GET['name']
        detail = self.request.GET['detail']
        number = self.request.GET['number']
        phone = self.request.GET['phone']
        pay = self.request.GET['pay']

        

        if email is not None:
            Command.objects.create( email =email, price=price, quantity=quantity, name=name,detail=detail, number=number, phone= phone, pay=pay ,active=active)
            return

class CommandUpdateAPIView(ModelViewSet):

    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = CommandSerializer
    queryset = Command.objects.all()
 
    def get_queryset(self):
        #email = self.request.GET['email']
        pay = self.request.GET['pay']
        active = self.request.GET['active']
        id = self.request.GET['id']
        if id is not None :
            command= Command.objects.get(pk=id)
            command.pay = pay
            command.save()
            return        



class TripAPIView(ModelViewSet):

    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)

    serializer_class = TripSerializer
    queryset = Trip.objects.all()
 
    def get_queryset(self):
        queryset = Trip.objects.filter(active=True)
        trip_email = self.request.GET.get('email')
        if trip_email is not None:
            queryset = queryset.filter(email=trip_email)


        return queryset


class TripCreateAPIView(ModelViewSet):

    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = TripSerializer
    queryset = Trip.objects.all()
 
    def get_queryset(self):
        email = self.request.GET['email']
        active = self.request.GET['active']
        departure = self.request.GET['departure']
        arrival = self.request.GET['arrival']
        phone = self.request.GET['phone']
        date_time = self.request.GET['date_time']
        if email is not None:
            Trip.objects.create( email =email, date_time=date_time ,phone=phone, departure=departure, arrival=arrival, active=active)
            return


class DeliveryPayAPIView(ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = DeliveryPaySerializer
    queryset = DeliveryPay.objects.filter(active=True)