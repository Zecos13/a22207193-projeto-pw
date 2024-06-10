from django.db import models

class Localizacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}"


class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Festival(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    bandas = models.ManyToManyField(Banda)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    imagem = models.ImageField()
    site = models.URLField(blank=True)

    def __str__(self):
        return self.nome