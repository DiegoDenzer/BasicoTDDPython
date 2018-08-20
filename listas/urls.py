from django.urls import path
from listas.views import home_page, lista, nova_lista

urlpatterns = [
    path('', home_page, name='home'),
    path('lista/new', nova_lista, name='nova_lista'),
    path('lista/lista-unica', lista , name='lista')
]