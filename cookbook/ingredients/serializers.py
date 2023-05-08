from rest_framework import routers, serializers, viewsets
from .models import Ingredient

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"