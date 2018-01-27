from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def logout_view(request):
    """" Faz o Logout do Usuário """
    logout(request)
    return HttpResponseRedirect(reverse('app:index'))
def register(request):
    """ Faz o cadastro de um novo usuário """
    if request.method != 'POST':
        #Exibe o formulário de cadastro em branco
        form = UserCreationForm()
    else:
        #Processa o formulário preenchido
        form = UserCreationForm (data = request.POST)
        if form.is_valid():
            new_user = form.save()
            # Faz o longin do usuário e redireciona para a página Inicial
            authenticated_user = authenticate(username=new_user, password = request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('app:index'))
    context = {'form' : form}
    return render (request, 'users/register.html',context)
