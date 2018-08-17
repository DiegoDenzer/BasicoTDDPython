from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'listas/home.html', {'novo_item': request.POST.get('tarefa', '')})