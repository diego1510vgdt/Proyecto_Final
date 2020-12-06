from django.urls import path
from .views import *

urlpatterns = [
    path('', home.as_view() , name="home"),
    path('mat/muestra', Mtr.as_view() , name="materia"),
    path('clss/muestra', Clss.as_view(), name="clase"),
    path('alm/muestra', Alm.as_view(), name="alumno"),
    path('mat/add', MtrAdd.as_view(), name="materiaAdd"),
    path('clss/add', ClssAdd.as_view(), name="claseAdd"),
    path('mat/<int:id>/', MtrUpdt.as_view(), name="materiaUpdt"),
]
