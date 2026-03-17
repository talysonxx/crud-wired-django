from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegistroUsuarioForm

# Create your views here.
def index(request):
    return render(request, 'usuarios/index.html')

def registrar(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada e login efetuado com sucesso!')
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registrar.html', {'form': form})

def custom_404(request, exception):
    return render(request, 'usuarios/404.html', status=404)
