from django.shortcuts import render  #libreria para realizar render del template
from django.shortcuts import redirect   #libreria para realizar la redireccion luego del login

from django.contrib import messages   #libreria para mostrar mensajes del servidor
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate   #libreria que nos permite validar los campos con el servidor
from .forms import RegisterForm   #importamos el formulario

from django.contrib.auth.models import User   #libreria para crear nuevos usuarios



# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'login':'login.html'
    })

def login_view(request):
    #bloqueando las urls
    if request.user.is_authenticated:
        return redirect('principal')

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
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login_v')

def register_view(request):
    #bloqueando las urls
    if request.user.is_authenticated:
        return redirect('principal')

    form = RegisterForm(request.POST or None)   #instanciamos a la clase que se encuentra en forms

    #leer los datos del formulario s
    if request.method == 'POST' and form.is_valid():
        #username = form.cleaned_data.get('username')
        #email = form.cleaned_data.get('email')
        #password = form.cleaned_data.get('password')

        user = form.save()#User.objects.create_user(username, email, password)  #crear usuarios pero no como admin
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('principal')

    return render(request, 'users/register.html', {
        'forms': form    #nombre con el que llamaremos en nuestr html
    })
