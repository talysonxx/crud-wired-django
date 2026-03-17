from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        # list all fields that should appear in the registration form
        fields = ('email', 'nome', 'sobrenome')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Força o campo sobrenome a ser obrigatório no formulário
        self.fields['sobrenome'].required = True
