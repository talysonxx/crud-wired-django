# The Wired - Retro Task Manager

*"A Wired não conhece limites. Este terminal foi construído como um repositório temporário de memórias digitais..."*

Este projeto é um CRUD (Create, Read, Update, Delete) de anotações e tarefas, construído em **Django**.
Ele foi projetado especificamente para atuar como um "bloco de notas" seguro e enigmático, possuindo um forte apelo visual inspirado na estética Cyberpunk/Synthwave e influências de animes clássicos como *Serial Experiments Lain*. 

Um usuário pode se registrar no sistema (Autenticação) e manter suas anotações exclusivas e vinculadas ao seu cadastro de maneira privada, com todo o registro acontecendo dentro desse falso terminal *neon*.

### 🎥 Showcase do Sistema
![Sistema CRUD The Wired em Ação](https://github.com/user-attachments/assets/4ea7faad-334f-439f-a16c-41f9ec0caecb)!


---

## 💻 Funcionalidades
- **Registro e Autenticação de Usuários**: Apenas usuários autenticados têm acesso ao terminal.
- **Isolamento de Dados**: Cada usuário vê e gerencia exclusivamente suas próprias anotações. Se um usuário tentar alterar forçadamente pela URL (Ex: `/tarefas/editar/5`) uma tarefa que não lhe pertence, o sistema negará acesso via um Erro 404 personalizado ("DADOS NÃO ENCONTRADOS").
- **CRUD Completo de Tarefas**:
  - **CREATE:** Adicione novos registros à rede.
  - **READ:** Visualize em modo terminal todos os relatórios pendentes ou concluídos.
  - **UPDATE:** Modifique assinaturas, status e detalhes.
  - **DELETE:** (Disponível conforme expansão do módulo).
- **Estética Customizada**: Tema Cyberpunk e Neon CSS Puro, com efeitos de Scaneamento Analógico (CRT lines), Glitch-texts, e responsividade.

---

## ⚙️ Como Instalar e Rodar Localmente (Testes)

Para pessoas clonando este repositório que desejem subir "The Wired" localmente, siga os passos abaixo:

### 1. Clonando o Repositório e Preparando o Ambiente
Abra o seu terminal e rode os comandos sequencialmente para baixar o projeto e instalar as bibliotecas necessárias:

```bash
# Clone este repositório
git clone <URL_DO_SEU_REPOSITORIO>

# Entre na pasta raiz do projeto clonado
cd <NOME_DA_PASTA>

# Crie um Ambiente Virtual Python
python -m venv venv

# Ative o Ambiente Virtual 
# (No Windows:)
.\venv\Scripts\Activate.ps1
# (No Linux/Mac:)
source venv/bin/activate

# Instale os pacotes e dependências (Django, etc):
pip install -r requirements.txt
```

### 2. Configurando o Ambiente e Banco de Dados (Variáveis `.env`)
O projeto utiliza a biblioteca `django-environ` para ocultar os dados sensíveis através de um arquivo `.env`. No momento em que baixar o projeto, você encontrará apenas um arquivo chamado `.env.example`.

1. **Faça uma cópia** do arquivo `.env.example` e renomeie-o para `.env` puro.
2. Abra o arquivo `.env` gerado.

**⚠️ Importante sobre o Banco de Dados:**
Por padrão e para uso em produção, o sistema está configurado para tentar se conectar a um banco de dados **PostgreSQL** usando as variáveis definidas no seu `.env` (Usuario,  Senha, Host etc). 

> **Para testes locais rápidos:** Se você quiser apenas rodar e testar o sistema agora mesmo **SEM** lidar com configuração do PostgreSQL, abra o arquivo `crud_antonio/settings.py`. Você verá o banco `django.db.backends.sqlite3` do próprio Django comentado no começo do bloco `DATABASES`. Basta descomentar as duas linhas do SQLite3 e deletar/comentar todas as outras linhas nativas (ENGINE, NAME, USER, PASSWORD...) da requisição do `env()`.

### 3. Migrações e Inicialização
Seja usando PostgreSQL ou SQLite3 temporário, aplique a estrutura dos dados com:

```bash
# Sincronize o banco de dados
python manage.py migrate

# Inicie o servidor em localhost
python manage.py runserver
```

### 4. Conectando...
Se tudo deu certo, a linha de comando exibirá sua porta. Abra seu navegador em:
👉 `http://127.0.0.1:8000/`

Crie o seu usuário clicando em *[ Sincronizar ]* e seja bem-vindo(a) de volta.
