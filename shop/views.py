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
from dotenv import load_dotenv

from shop.models import Category, Code, DeliveryPay, Paiement, Product, User, Command, Trip
from shop.serializers import CategorySerializer, CodeSerializer, DeliveryPaySerializer, PaiementSerializer, ProductSerializer, UserSerializer, CommandSerializer, TripSerializer

from django.http import HttpResponse
from django.template import loader
from mailjet_rest import Client
import os
load_dotenv()

def mail(email : str):
   send_mail(subject='A cool subject',message='A stunning message',from_email='sargal@jendgroup.com',recipient_list=[email])


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

    def create(self, request, *args, **kwargs):
        response = super(PaiementCreateAPIView, self).create(request, *args, **kwargs)
        send_mail(
                subject=f"Command N° : {self.request.GET['number']} Livrée",
                message='SARGAL',
                html_message = f"<p>Bonjour, </br> \
                    L'équipe SARGAL vous remercie de passer votre commande via notre Application. </p>\
                    <p>Félicitations. Votre commande a été livrée.</br> \
                    <p> Sargal vous remercie infiniment. </p> \
                    <h5> Détails de votre commande </h5> \
                    <p>N° de commande :{self.request.GET['number']} </p> \
                    <p> Paiement : {self.request.GET['paiement']}</p> \
                    <p> Pour toutes modifications ou réclamations veuillez contacter directement notre service clientel via  l'application </p>",
                from_email='sargal@jendgroup.com',
                recipient_list=[self.request.GET['email']])
        print(f"Message send to {self.request.GET['email']}")
        return response

 
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

    def create(self, request, *args, **kwargs):
        response = super(UserCreateAPIView, self).create(request, *args, **kwargs)
        send_mail(
                subject=f"Bienvenue {self.request.GET['firs_name']} {self.request.GET['last_name']}",
                message='SARGAL',
                html_message = f"<p>Bonjour, </br> \
                    L'équipe SARGAL est très heureuse de vous acceuillir parmis nous</p>\
                    <p>Vous avez reçu un email pour valider votre adresse eamil et ainsi accéder à toutes les fonctionnalités de l'application.</p> \
                    <p> Sargal vous remercie infiniment. </p> \
                    <h5> Voici les informations que vous avez remplis </h5> \
                    <p> Prénom : {self.request.GET['firs_name']} </p> \
                    <p> Nom : {self.request.GET['last_name']} </p> \
                    <p> Téléphone :{self.request.GET['phone']} </p> \
                    <p> Adresse :{self.request.GET['address']} </p> \
                    <p> Email :{self.request.GET['email']} </p> \
                    <p> Pour toutes modifications ou réclamations veuillez contacter directement notre service clientel via  l'application </p>",
                from_email='sargal@jendgroup.com',
                recipient_list=[self.request.GET['email']])
        print(f"Message send to {self.request.GET['email']}")
        return response
 
    def get_queryset(self):
        email = self.request.GET['email']
        firs_name = self.request.GET['firs_name']
        last_name = self.request.GET['last_name']
        gender = self.request.GET['gender']
        date_of_birth = self.request.GET['date_of_birth']
        phone = self.request.GET['phone']
        address = self.request.GET['address']
        card_money = self.request.GET['card_money']
        customer = self.request.GET['customer']
        active = self.request.GET['active']
        if email is not None:
            User.objects.get_or_create(email=email,firs_name =firs_name,last_name= last_name, gender=gender, date_of_birth=date_of_birth , phone= phone,address= address, card_money=card_money, customer=customer, active=active)

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

    def create(self, request, *args, **kwargs):
        response = super(CommandCreateAPIView, self).create(request, *args, **kwargs)
        send_mail(
                subject=f"Command N° : {self.request.GET['number']}",
                message='SARGAL',
                html_message = f"<p>Bonjour, </br> \
                    L'équipe SARGAL vous remercie de passer votre commande via notre Application. </p>\
                    <p>Votre command est en cours de validation. Vous recevrez une notification dès qu'il sera validé.</p> \
                    <p> Sargal vous remercie infiniment. </p> \
                    <h5> Détails de votre commande </h5> \
                    <p> Détails : {self.request.GET['detail']} </p> \
                    <p>N° de commande :{self.request.GET['number']} </p> \
                    <p> Téléphone :{self.request.GET['phone']} </p> \
                    <p> Total (dont frais de livraion) : {self.request.GET['price']} MRU </p> \
                    <p> Pour toutes modifications ou réclamations veuillez contacter directement notre service clientel via  l'application </p>",
                from_email='sargal@jendgroup.com',
                recipient_list=[self.request.GET['email']])
        print(f"Message send to {self.request.GET['email']}")
        return response

 
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

class CommandUpdateValidateAPIView(ModelViewSet):

    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = CommandSerializer
    queryset = Command.objects.all()
    lookup_field='pk'
 
    def get_queryset(self):
        
        active = self.request.GET['active']
        validate = self.request.GET['validate']
        id = self.request.GET['id']
        number = self.request.GET['number']
        email = self.request.GET['email']
        price = self.request.GET['price']
        if email is not None :
            command= Command.objects.get(pk=id)
            command.validate = validate
            command.price = price
            command.save()
            send_mail(
                subject=f"Command N° : {self.request.GET['number']} Validé",
                message='SARGAL',
                html_message = f"<p>Bonjour, </br> \
                    L'équipe SARGAL vous remercie de passer votre commande via notre Application. </p>\
                    <p>Félicitations. Votre commande a été validée est en cours de préparation et vous sera livré dans les meilleurs délais. </br> \
                    Notre service de livraison vous contactera pour définir avec vous le mode de livraison.</p> \
                    <p> Sargal vous remercie infiniment. </p> \
                    <h5> Détails de votre commande </h5> \
                    <p>N° de commande :{number} </p> \
                    <p> Pour toutes modifications ou réclamations veuillez contacter directement notre service clientel via  l'application </p>",
                from_email='sargal@jendgroup.com',
                recipient_list=[self.request.GET['email']])
            print(f"Message send to {self.request.GET['email']}")
            return   

class CommandUpdateAcceptedAPIView(ModelViewSet):

    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,)


    serializer_class = CommandSerializer
    queryset = Command.objects.all()
        

    
 
    def get_queryset(self):
        active = self.request.GET['active']
        accepted = self.request.GET['accepted']
        id = self.request.GET['id']
        number = self.request.GET['number']
        email = self.request.GET['email']
        if id is not None :
            send_mail(
                subject=f"Command N° : {self.request.GET['number']} Annulée",
                message='SARGAL',
                html_message = f"<p>Bonjour, </br> \
                    L'équipe SARGAL vous remercie de passer votre commande via notre Application. </p>\
                    <p>Malheursement votre commande a été annulée. </br> \
                    Si vous avez payé avec Sargal Cash, vous serez remboursé dans 5 jours ouvrés. <br> \
                    Vérifier votre compte sargal Cash.</p> \
                    <h5> Détails de votre commande </h5> \
                    <p>N° de commande :{self.request.GET['number']} </p> \
                    <p> Pour toutes modifications ou réclamations veuillez contacter directement notre service clientel via  l'application </p>",
                from_email='sargal@jendgroup.com',
                recipient_list=[self.request.GET['email']])
            print(f"Message send to {self.request.GET['email']}")
            command= Command.objects.get(pk=id)
            command.accepted = accepted
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