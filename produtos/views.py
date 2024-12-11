from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

def ver_produtos(request):
    if request.method == 'GET':
        nome = 'Paulo Helder Fernandes'
        produto = Produto.objects.all()
        return render(request,'ver_produtos.html', {'nome':nome, 'produto':produto})
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        produto = Produto(nome=nome, idade=idade)
        produto.save()
        return HttpResponse('Cadastro feito com sucesso')

def inserir_produto(request):
    return HttpResponse('Estou no Inserir Produto')

