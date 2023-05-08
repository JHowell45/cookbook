from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import IngredientSerializer
from .models import Ingredient

# Create your views here.
class IngredientViewSet(viewsets.ViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer