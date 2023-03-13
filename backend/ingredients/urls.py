from django.urls import path 
from . import views

# define the urls
urlpatterns = [
    path('ingredients/', views.ingredients),
    path('ingredients/<int:pk>/', views.ingredient_detail),
]