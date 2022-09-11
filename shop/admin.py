from django.contrib import admin
from shop.models import Category, Code, DeliveryPay, Paiement, Product, User, Command, Trip


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'active')


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'category','description','price','amount','photo','promotion', 'active')


"""class ArticleAdmin(admin.ModelAdmin):

    list_display = ('name', 'product', 'category','price' ,'amount','photo','promotion','active')

    @admin.display(description='Category')
    def category(self, obj):
        return obj.product.category"""

class UserAdmin(admin.ModelAdmin):

    list_display = ('email','gender','date_of_birth','firs_name', 'last_name',  'phone', 'card_money', 'address','customer', 'delivery','seller', 'validator' ,'active' ) 

class CommandAdmin(admin.ModelAdmin):

    list_display = ('email','name', 'price', 'quantity', 'detail','validate', 'accepted','number' ,'phone','pay' ,'active' )

class TripAdmin(admin.ModelAdmin):

    list_display = ('departure','arrival','email', 'phone','date_time','active' )

class CodeAdmin(admin.ModelAdmin):

    list_display = ('date_created','date_updated','email','code', 'amount','recharge','active' )

class PaiementAdmin(admin.ModelAdmin):

    list_display = ('date_created','date_updated','email','number', 'delivery','paiement','name','active' )

class DeliveryPayAdmin(admin.ModelAdmin):

    list_display = ('date_created','date_updated','delivery_pay', 'name','active' )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
#admin.site.register(Article, ArticleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Command, CommandAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(Code, CodeAdmin)
admin.site.register(Paiement, PaiementAdmin)
admin.site.register(DeliveryPay, DeliveryPayAdmin)