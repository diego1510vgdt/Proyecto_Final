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

class ClssUpdt(View):
    def get(self, request):
        clase = Clase.objects.get(id=id)
        form = ClaseForm(instance=clase)
        context = {'form': form}
        return render(request, 'clases_add.html', context)
    
    def post(self,request):
        clase = Clase.objects.get(id=id)
        form = ClaseForm(request.POST, instance=clase)
        if form.is_valid():
            form.save()
            return redirect('clase')
        else:
            context = {'form': form}
            return render(request, 'clases_add.html', context)

class Alm(View):
    def get(self, request):
        alumnos = Alumno.objects.all()
        for al in alumnos:
            print(al)
        context = {'alumnos' : alumnos}
        return render(request, 'alumno.html', context)

class AlmAdd(View):
    def get(self, request):
        form = AlumnoForm()
        context = {'form': form}
        return render(request, 'alumno_add.html', context)
    
    def post(self,request):
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno')
        else:
            form = AlumnoForm()
            context = {'form': form}
            return render(request, 'alumno_add.html', context)

class AlmUpdt(View):
    def get(self, request):
        alumno = Alumno.objects.get(id=id)
        form = AlumnoForm(instance=alumno)
        context = {'form': form}
        return render(request, 'alumno_add.html', context)
    
    def post(self,request):
        alumno = Alumno.objects.get(id=id)
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('alumno')
        else:
            context = {'form': form}
            return render(request, 'alumno_add.html', context)

class Prof(View):
    def get(self, request):
        profesores = Profesor.objects.all()
        for prof in profesores:
            print(prof)
        context = {'profesores' : profesores}
        return render(request, 'profesor.html', context)

class ProfAdd(View):
    def get(self, request):
        form = ProfesorForm()
        context = {'form': form}
        return render(request, 'profesor_add.html', context)
    
    def post(self,request):
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesor')
        else:
            form = ProfesorForm()
            context = {'form': form}
            return render(request, 'profesor_add.html', context)

class ProfUpdt(View):
    def get(self, request):
        profesor = Profesor.objects.get(id=id)
        form = ProfesorForm(instance=profesor)
        context = {'form': form}
        return render(request, 'profesor_add.html', context)
    
    def post(self,request):
        profesor = Profesor.objects.get(id=id)
        form = AlumnoForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('profesor')
        else:
            context = {'form': form}
            return render(request, 'profesor_add.html', context)

class Asis(View):
    def get(self, request):
        asistencias = Asistencia.objects.all()
        for asis in asistencias:
            print(asis)
        context = {'asistencias' : asistencias}
        return render(request, 'asistencia.html', context)

class AsisAdd(View):
    def get(self, request):
        form = AsistenciaForm()
        context = {'form': form}
        return render(request, 'asistencia_add.html', context)
    
    def post(self,request):
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asistencia')
        else:
            form = AsistenciaForm()
            context = {'form': form}
            return render(request, 'asistencia_add.html', context)

class AsisUpdt(View):
    def get(self, request):
        asistencia = Asistencia.objects.get(id=id)
        form = AsistenciaForm(instance=asistencia)
        context = {'form': form}
        return render(request, 'asistencia_add.html', context)
    
    def post(self,request):
        asistencia = Asistencia.objects.get(id=id)
        form = AsistenciaForm(request.POST, instance=asistencia)
        if form.is_valid():
            form.save()
            return redirect('asistencia')
        else:
            context = {'form': form}
            return render(request, 'asistencia_add.html', context)
