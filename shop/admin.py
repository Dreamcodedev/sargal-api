from django.contrib import admin
from shop.models import Category, Product, Article, User, Command


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'active')


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'category', 'active')


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('name', 'product', 'category','price' ,'amount','photo','active')

    @admin.display(description='Category')
    def category(self, obj):
        return obj.product.category

class UserAdmin(admin.ModelAdmin):

    list_display = ('firs_name', 'last_name', 'email', 'phone', 'card_money', 'active' )


class CommandAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'quantity', 'user','active' )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Command, CommandAdmin)
