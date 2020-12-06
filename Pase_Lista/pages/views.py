from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *

# Create your views here.

class home(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context)

class Mtr(View):
    def get(self, request):
        materias = Materia.objects.all()
        for mat in materias:
            print(mat)
        context = {'materias' : materias}
        return render(request, 'materias.html', context)

class Clss(View):
    def get(self, request):
        clases = Clase.objects.all()
        for clss in clases:
            print(clss)
        context = {'clases' : clases}
        return render(request, 'clases.html', context)

class Alm(View):
    def get(self, request):
        alumnos = Alumno.objects.all()
        for al in alumnos:
            print(al)
        context = {'clases' : alumnos}
        return render(request, 'alumno.html', context)