from django.db import models, transaction
from phone_field import PhoneField


class Category(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    #photo=models.ImageField(upload_to='cars', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField(default=1)
    photo=models.ImageField(upload_to='products', blank=True)
    promotion = models.BooleanField(default=False)

    category = models.ForeignKey('shop.Category', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


"""class Article(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField(default=1)
    photo=models.ImageField(upload_to='articles', blank=True)
    promotion = models.BooleanField(default=False)

    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.name"""

class User(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)

    firs_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length = 254, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number', null=True) 
    card_money = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    customer = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    seller = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Command(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)

    name = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(default=1)
    email =  models.EmailField(max_length = 254, null=True)
    detail = models.TextField(blank=True)
    validate = models.BooleanField(default=False)
    accepted = models.BooleanField(default=True)
    pay = models.BooleanField(default=False)
    number = models.PositiveIntegerField(default=1)
    phone = models.PositiveIntegerField(default=0)




    def __str__(self):
        return self.name

class Trip(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)
    date_time=models.CharField(max_length=255)
    departure = models.CharField(max_length=255)
    arrival = models.CharField(max_length=255)
    phone = PhoneField(blank=True, help_text='Contact phone number', null=True)
    email =  models.EmailField(max_length = 254, null=True)


    def __str__(self):
        return self.email

class Code(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)
    email =  models.EmailField(max_length = 254, null=True)
    code = models.PositiveIntegerField(default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    recharge = models.BooleanField(default=False)


    def __str__(self):
        return self.email

class Paiement(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)
    number = models.PositiveIntegerField(default=1)
    delivery =  models.BooleanField(default=False)
    paiement = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length = 254, null=True)
    name = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return self.email

class DeliveryPay(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)
    name = models.CharField(max_length=255, blank=True)
    delivery_pay = models.DecimalField(max_digits=10, decimal_places=2, null=True)


    def __str__(self):
        return self.name

