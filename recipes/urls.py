# recipes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipes/<int:pk>/edit/', views.edit_recipe, name='edit_recipe'),
]
