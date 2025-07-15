from django.urls import path
from . import views

urlpatterns = [
    path('ids/', views.lista_ids, name='lista_ids'),
    path('id-title/', views.lista_id_title, name='lista_id_title'),
    path('sin-resolver/', views.sin_resolver, name='sin_resolver'),
    path('resueltos/', views.resueltos, name='resueltos'),
    path('id-user/', views.lista_id_user, name='lista_id_user'),
    path('resueltos-id-user/', views.resueltos_id_user, name='resueltos_id_user'),
    path('sin-resolver-id-user/', views.sin_resolver_id_user, name='sin_resolver_id_user'),
]
