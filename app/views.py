from django.shortcuts import render,redirect
from .forms import TarefasForm
from .models import Tarefas

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        tarefas_form = TarefasForm(request.POST)
        if tarefas_form.is_valid():
            tarefas_form.save()
            return redirect('listar')
    else :
        tarefas_form = TarefasForm()
    tarefas_form = TarefasForm()
    return render(request,'forms_cadastro.html',{'tarefas_form': tarefas_form })
def listar(request):
    tarefas = Tarefas.objects.all()

    return render(request,'listagem.html',{'tarefas':tarefas})