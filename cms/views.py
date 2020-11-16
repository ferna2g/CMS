from django.shortcuts import render  #libreria para realizar render del template
from django.shortcuts import redirect   #libreria para realizar la redireccion luego del login

from django.contrib import messages   #libreria para mostrar mensajes del servidor
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate   #libreria que nos permite validar los campos con el servidor


# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'login':'login.html'
    })

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        #validamos si se encuentra en la base de datos
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('principal')
        else:
            messages.error(request, 'Usuario o Contrase;a incorrecta')

    return render(request, 'users/login.html', {

    })

def logout_view(request):
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login_v')
