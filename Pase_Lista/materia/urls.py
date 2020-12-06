from django.urls import path
from .views import *

urlpatterns = [
    path('', materiaView, name="materia")
]