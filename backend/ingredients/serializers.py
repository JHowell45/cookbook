from rest_framework import serializers,routers,viewsets
from models import Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id','name','description','price','image', 'created_at', 'updated_at')