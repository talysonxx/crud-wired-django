from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tarefas/adicionar', views.adicionarTarefa, name='adicionar'),
    path('tarefas/editar/<tarefa_id>', views.editarTarefa, name='tarefa'),
]
