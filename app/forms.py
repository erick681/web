from django import forms
from .models import Tarefas

class TarefasForm(forms.ModelForm):
    class Meta:
        model = Tarefas 
        fields = '__all__'
        widgets = {
            "data": forms.DateInput(attrs={'type':'date'})
        }