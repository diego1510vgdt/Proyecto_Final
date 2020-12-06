from django.urls import path
from .views import *

urlpatterns = [
    path('', alumnoView, name="alumno")
]