from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Pendiente
import requests

# URL de la API externa (ejemplo, puedes cambiarla)
API_URL = 'https://jsonplaceholder.typicode.com/todos'

# Sincroniza datos de la API a la BD local
def obtener_pendientes_api():
    response = requests.get(API_URL)
    if response.status_code == 200:
        for item in response.json():
            Pendiente.objects.update_or_create(
                id=item['id'],
                defaults={
                    'title': item['title'],
                    'user_id': item['userId'],
                    'completed': item['completed'],
                }
            )

# Lecturas desde API
def lista_ids(request):
    obtener_pendientes_api()
    pendientes = Pendiente.objects.all().values('id')
    return render(request, 'pendientes/lista.html', {'pendientes': pendientes, 'campos': ['id']})

def lista_id_title(request):
    obtener_pendientes_api()
    pendientes = Pendiente.objects.all().values('id', 'title')
    return render(request, 'pendientes/lista.html', {'pendientes': pendientes, 'campos': ['id', 'title']})

def sin_resolver(request):
    pendientes = Pendiente.objects.filter(completed=False).values('id', 'title')
    return render(request, 'pendientes/lista.html', {'pendientes': pendientes, 'campos': ['id', 'title']})

def resueltos(request):
    pendientes = Pendiente.objects.filter(completed=True).values('id', 'title')
    return render(request, 'pendientes/lista.html', {'pendientes': pendientes, 'campos': ['id', 'title']})

def lista_id_user(request):
    pendientes = Pendiente.objects.all().values('id', 'user_id')
    return render(request, 'pendientes/lista.html', {'pendientes': pendientes, 'campos': ['id', 'user_id']})

def resueltos_id_user(request):
    pendientes = Pendiente.objects.filter(completed=True).values('id', 'user_id')
    return render(request, 'pendientes/lista.html', {'pendientes': pendientes, 'campos': ['id', 'user_id']})

def sin_resolver_id_user(request):
    pendientes = Pendiente.objects.filter(completed=False).values('id', 'user_id')
    return render(request, 'pendientes/lista.html', {'pendientes': pendientes, 'campos': ['id', 'user_id']})


# ----------------------------
# CRUD LOCAL (Create, Update, Delete)
# ----------------------------

# Formulario para crear y editar
class PendienteForm(forms.ModelForm):
    class Meta:
        model = Pendiente
        fields = ['id', 'title', 'user_id', 'completed']

# Crear pendiente
def crear_pendiente(request):
    form = PendienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_id_title')
    return render(request, 'pendientes/formulario.html', {'form': form, 'accion': 'Crear'})

# Editar pendiente
def editar_pendiente(request, pk):
    pendiente = get_object_or_404(Pendiente, pk=pk)
    form = PendienteForm(request.POST or None, instance=pendiente)
    if form.is_valid():
        form.save()
        return redirect('lista_id_title')
    return render(request, 'pendientes/formulario.html', {'form': form, 'accion': 'Editar'})

# Eliminar pendiente
def eliminar_pendiente(request, pk):
    pendiente = get_object_or_404(Pendiente, pk=pk)
    if request.method == 'POST':
        pendiente.delete()
        return redirect('lista_id_title')
    return render(request, 'pendientes/eliminar.html', {'pendiente': pendiente})
