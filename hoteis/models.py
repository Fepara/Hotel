from django.db import models

class Hotel(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)
    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
