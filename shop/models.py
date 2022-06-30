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
    amount = models.PositiveSmallIntegerField(default=1)
    photo=models.ImageField(upload_to='articles', blank=True)
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
    amount = models.PositiveSmallIntegerField(default=1)
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
    email = models.EmailField(max_length = 254, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number', null=True) 
    card_money = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.email


class Command(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=1)
    email =  models.EmailField(max_length = 254, null=True)


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

