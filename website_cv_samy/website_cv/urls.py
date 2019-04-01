from django.urls import path
from . import views

urlpatterns = [
    path('index', views.home),
    path('', views.view_profesionnalExperience, name='accueil'),
    path('portfolio/<id_project>', views.view_portfolio),
]