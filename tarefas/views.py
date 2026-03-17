from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from . import forms

# Create your views here.
@login_required
def home(request):
    context = {
        'tarefas': Tarefa.objects.filter(dono_tarefa=request.user).order_by('data_criacao')
    }
    return render(request, 'tarefas/index.html', context)

@login_required
def adicionarTarefa(request):
    if request.method != 'POST':
        form = forms.AdicionarTarefaForm()
    else:
        form = forms.AdicionarTarefaForm(request.POST)
        if form.is_valid():
            nova_tarefa = form.save(commit=False)
            nova_tarefa.dono_tarefa = request.user
            nova_tarefa.save()
            return redirect('home')
    contexto = {
        'form': form
    }
    return render(request, 'tarefas/adicionar.html', contexto)

def editarTarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    if tarefa.dono_tarefa != request.user:
        return redirect('home')
    if request.method != 'POST':
        form = forms.AdicionarTarefaForm(instance=tarefa)
    else:
        form = forms.AdicionarTarefaForm(instance=tarefa, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    contexto = {
        'tarefa': tarefa,
        'form': form
    }
    return render(request, 'tarefas/editar_tarefa.html', contexto)