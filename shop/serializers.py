from django.db.models import fields
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from shop.models import Category, Code, DeliveryPay, Paiement, Product, User, Command, Trip

class CategorySerializer(ModelSerializer):

    # En utilisant un `SerializerMethodField', il est nécessaire d'écrire une méthode
    # nommée 'get_XXX' où XXX est le nom de l'attribut, ici 'products'
    products = SerializerMethodField()
    
    class Meta :
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']

    def get_products(self, instance):
        # Le paramètre 'instance' est l'instance de la catégorie consultée.
        # Dans le cas d'une liste, cette méthode est appelée autant de fois qu'il y a
        # d'entités dans la liste

        # On applique le filtre sur notre queryset pour n'avoir que les produits actifs
        queryset = instance.products.filter(active=True)
        # Le serializer est créé avec le queryset défini et toujours défini en tant que many=True
        serializer = ProductSerializer(queryset, many=True)
        # la propriété '.data' est le rendu de notre serializer que nous retournons ici
        return serializer.data

    def validate_name(self, value):
        # Nous vérifions que la catégorie existe
        if Category.objects.filter(name=value).exists():
        # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError('Category already exists')
        return value


class ProductSerializer(ModelSerializer):
    #articles = SerializerMethodField()

    class Meta :
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category','description','price','amount','photo','promotion','active' ]

class UserSerializer(ModelSerializer):

    class Meta :
        model = User
        fields = ['id', 'date_created', 'date_updated', 'firs_name','last_name','gender', 'date_of_birth' ,'address','email','phone','card_money', 'customer','delivery' ,'seller', 'validator' ,'active'] 



class CommandSerializer(ModelSerializer):

    class Meta :
        model = Command
        fields = ['id', 'date_created', 'date_updated', 'name','active', 'price','quantity','email', 'detail', 'validate', 'number','accepted', 'phone', 'pay']




class TripSerializer(ModelSerializer):

    class Meta :
        model = Trip
        fields = ['id', 'date_created', 'date_updated', 'active', 'departure','arrival','date_time','email', 'phone']

class CodeSerializer(ModelSerializer):

    class Meta :
        model = Code
        fields = ['id', 'date_created','date_updated','email','code', 'amount','recharge','active']    

class PaiementSerializer(ModelSerializer):

    class Meta :
        model = Paiement
        fields = ['date_created','date_updated','email','number', 'delivery','paiement','name','active']

class DeliveryPaySerializer(ModelSerializer):

    class Meta :
        model = DeliveryPay
        fields = ['date_created','date_updated','delivery_pay', 'name' ,'active']