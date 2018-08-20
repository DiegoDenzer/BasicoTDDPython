from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from listas.models import Item


def home_page(request):

    if request.method == 'POST':
        item = Item.objects.create(texto=request.POST['tarefa'])
        return redirect('lista/lista-unica')

    itens = Item.objects.all()
    return render(request, 'listas/home.html', {'itens':  itens })

def lista(request):
    itens = Item.objects.all()
    return render(request, 'listas/lista.html', {'itens': itens})

def nova_lista(request):
    item = Item.objects.create(texto=request.POST['tarefa'])
    return redirect('lista/lista-unica')