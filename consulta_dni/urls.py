from django.urls import path
from . import views

urlpatterns = [
    path('', views.consulta_dni, name='consulta_dni'),
]