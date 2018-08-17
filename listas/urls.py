from django.urls import path
from listas.views import home_page, lista

urlpatterns = [
    path('', home_page, name='home'),
    path('lista/lista-unica', lista , name='lista')
]