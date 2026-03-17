from django import forms
from . import models

class AdicionarTarefaForm(forms.ModelForm):
    class Meta:
        model = models.Tarefa
        fields = ['nome', 'descricao', 'status']