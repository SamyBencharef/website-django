from django.urls import path
from . import views

urlpatterns = [
    path('index', views.home),
    path('', views.view_profesionnalExperience),
    path('portfolio/<id_project>', views.view_portfolio),
]