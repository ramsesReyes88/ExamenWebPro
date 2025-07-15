from django.shortcuts import render
from .models import Pendiente
import requests

API_URL = 'https://jsonplaceholder.typicode.com/todos'  # usa la API real de Parra's Dev si tienes otra

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
