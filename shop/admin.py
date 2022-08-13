from django.contrib import admin
from shop.models import Category, Product, User, Command, Trip


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

    list_display = ('email','firs_name', 'last_name',  'phone', 'card_money', 'address', 'active' )


class CommandAdmin(admin.ModelAdmin):

    list_display = ('email','name', 'price', 'quantity', 'detail','delivery','validate', 'active' )

class TripAdmin(admin.ModelAdmin):

    list_display = ('departure','arrival','email', 'phone','date_time','active' )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
#admin.site.register(Article, ArticleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Command, CommandAdmin)
admin.site.register(Trip, TripAdmin)