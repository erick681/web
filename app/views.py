from django.shortcuts import render
from .forms import TarefasForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        tarefas_form(request.POST)
        if tarefas_form.is_valid():
            tarefas_form.save()
    else :
        tarefas_form = TarefasForm()
    tarefas_form = TarefasForm()
    return render(request,'forms_cadastro.html',{'tarefas_form': tarefas_form })
