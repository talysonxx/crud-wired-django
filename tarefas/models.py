from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Usuario

# Create your models here.
class Tarefa(models.Model):
    nome = models.CharField(_("Nome"), max_length=254)
    descricao = models.TextField(_("Descrição"), null=True, blank=True)
    status = models.BooleanField(_("Completo"), default=False)
    data_criacao = models.DateTimeField(_("Data de criação"), auto_now_add=True)
    dono_tarefa = models.ForeignKey(Usuario, verbose_name=_("Dono"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Tarefa')
        verbose_name_plural = _('Tarefas')

    def __str__(self):
        return f'{self.nome} - {self.status}'
