from django.urls import path
from .views import *

urlpatterns = [
    path('', home.as_view() , name="home"),
    path('mat/muestra', Mtr.as_view() , name="materia"),
    path('clss/muestra', Clss.as_view(), name="clase"),
    path('alm/muestra', Alm.as_view(), name="alumno")
]
