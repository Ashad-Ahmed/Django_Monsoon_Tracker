from rest_framework import serializers
from myapp.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        #fields = '__all__' 
        exclude = ['id', 'name']