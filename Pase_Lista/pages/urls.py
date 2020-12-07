from django.urls import path
from .views import *

urlpatterns = [
    path('', home.as_view() , name="home"),
    path('mat/muestra', Mtr.as_view() , name="materia"),
    path('mat/add', MtrAdd.as_view(), name="materiaAdd"),
    path('mat/<int:id>/', MtrUpdt.as_view(), name="materiaUpdt"),
    path('clss/muestra', Clss.as_view(), name="clase"),
    path('clss/add', ClssAdd.as_view(), name="claseAdd"),
    path('clss/<int:id>', ClssUpdt.as_view(), name="claseUpdt"),
    path('alm/muestra', Alm.as_view(), name="alumno"),
    path('alm/add', AlmAdd.as_view(), name="alumnoAdd"),
    path('alm/<int:id>', AlmUpdt.as_view(), name="alumnoUpdt"),
    path('prof/muestra', Prof.as_view(), name="profesor"),
    path('prof/add', ProfAdd.as_view(), name="profesorAdd"),
    path('prof/<int:id>', ProfUpdt.as_view(), name="profesorUpdt"),
    path('asis/muestra', Asis.as_view(), name="asistencia"),
    path('asis/add', AsisAdd.as_view(), name="asistenciaAdd"),
    path('asis/<int:id>', AsisUpdt.as_view(), name="asistenciaUpdt")
]
