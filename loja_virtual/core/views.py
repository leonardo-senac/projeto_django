from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def cadastrar_cliente_endereco(request):
    # Puxando os dados do endereço e cadastrando ele
    nova_rua = request.POST.get('rua')
    novo_bairro = request.POST.get('bairro')
    nova_cidade = request.POST.get('cidade')
    novo_numero = request.POST.get('numero')
    novo_complemento = request.POST.get('complemento')


    # Puxando os dados do cliente e cadastrando ele já com o novo endereco

    novo_nome = request.POST.get('nome_cliente')
    novo_cpf = request.POST.get('cpf')
    novo_email = request.POST.get('email')
    novo_telefone = request.POST.get('telefone')
    novo_nascimento = request.POST.get('data_nascimento')

    novo_endereco = Endereco.objects.create(rua=nova_rua, bairro=novo_bairro, cidade=nova_cidade, numero=novo_numero, complemento=novo_complemento)
    Cliente.objects.create(nome=novo_nome, cpf=novo_cpf, email=novo_email, telefone=novo_telefone, data_nascimento=novo_nascimento, endereco=novo_endereco)

    return redirect(lista_clientes)


def lista_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def cadastrar_produto(request):
    novo_nome = request.POST.get('nome_produto')
    nova_descricao = request.POST.get('descricao')
    novo_preco = request.POST.get('preco')
    novo_estoque = request.POST.get('estoque')
    id_categoria = request.POST.get('categoria')
    nova_categoria = Categoria.objects.get(id=id_categoria)

    Produtos.objects.create(nome=novo_nome, descreicao=nova_descricao, preco=novo_preco, estoque=novo_estoque, categoria=nova_categoria)

    return render(lista_clientes)

def cadastrar_categoria(request):
    novo_nome = request.POST.get('nome_categoria')

    Categoria.objects.create(nome=novo_nome)

    return redirect(lista_produtos)