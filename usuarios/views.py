from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    form = LoginForms()

    # Garante que o metodo de entrda é do tipo POST
    if request.method == 'POST':
        # Pega o formulario com os campos enviados no POST
        form = LoginForms(request.POST)
        # Valida o formulario
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
        # Cria um usuario com os dados vindos do formulario
        # e valida que pode ser feito o login
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        # Verifica se os dados não estão vazios
        if usuario is not None:
            # Faz a autenticação
            auth.login(request, usuario)
            return redirect ('index')
        else:
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form' : form})


def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
    
    # Valida se o formulario é valido
    if form.is_valid():
        # Verifica as senhas digitadas são diferentes
        if form['senha'].value() != form['confirmar_senha'].value():
            return redirect('cadastro')
        
        # Recupera os campos do formulario
        nome = form['nome_cadastro'].value()
        email = form['email'].value()
        senha = form['senha'].value()

        # Verifica dentro da tabela interna do Django 
        # se um usuario existe
        if User.objects.filter(username=nome).exists():
            return redirect('cadastro')
        
        # Cria um usuario e salva dentro do banco interno do Django
        usuario = User.objects.create_user(
            username=nome,
            email=email,
            password=senha
        )

        usuario.save()
        return redirect('login')        

    return render(request, 'usuarios/cadastro.html', {'form' : form})
