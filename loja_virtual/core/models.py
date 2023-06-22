from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_edicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    estoque = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_edicao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='imagens_produtos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=70)
    cidade = models.CharField(max_length=50)
    complemento= models.TextField()
    numero = models.CharField(max_length=15)

    def __str__(self): # mudar a visualização da classe
        return f"{self.rua}, {self.numero}, {self.bairro}"

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=14)
    data_inscricao = models.DateTimeField()
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.nome}"


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateField()
    produtos = models.ManyToManyField(Produtos)