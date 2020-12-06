from django.shortcuts import *
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *
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

class MtrAdd(View):
    def get(self, request):
        form = MateriaForm()
        context = {'form': form}
        return render(request, 'materias_add.html', context)
    
    def post(self,request):
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materia')
        else:
            form = MateriaForm()
            context = {'form': form}
            return render(request, 'materias_add.html', context)

class MtrUpdt(View):
    def get(self, request, id):
        materia = Materia.objects.get(id=id)
        form = MateriaForm(instance = materia)
        context = {'form': form}
        return render(request, 'materias_add.html', context)
    
    def post(self,request, id):
        materia = Materia.objects.get(id=id)
        form = MateriaForm(request.POST, instance = materia)
        if form.is_valid():
            form.save()
            return redirect('materia')
        else:
            context = {'form': form}
            return render(request, 'materias_add.html', context)

class Clss(View):
    def get(self, request):
        clases = Clase.objects.all()
        for clss in clases:
            print(clss)
        context = {'clases' : clases}
        return render(request, 'clases.html', context)

class ClssAdd(View):
    def get(self, request):
        form = ClaseForm()
        context = {'form': form}
        return render(request, 'clases_add.html', context)
    
    def post(self,request):
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clase')
        else:
            form = MateriaForm()
            context = {'form': form}
            return render(request, 'clases_add.html', context)

class Alm(View):
    def get(self, request):
        alumnos = Alumno.objects.all()
        for al in alumnos:
            print(al)
        context = {'clases' : alumnos}
        return render(request, 'alumno.html', context)