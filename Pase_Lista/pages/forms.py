from django import forms
from .models import *

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'