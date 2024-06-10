from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()
    disciplinas = disciplinas = models.ManyToManyField('Disciplina', related_name='cursos')

    def __str__(self):
        return self.nome


class AreaCientifica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ects = models.IntegerField()
    curricularIUnitCode = models.CharField(max_length=100)
    areaCientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    conceitosAplicados = models.TextField()
    tecnologiasUsadas = models.TextField()
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='projeto_images', null=True, blank=True)
    linkVideo = models.URLField(null=True, blank=True)
    linkGithub = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome


class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=100)
    projetos = models.ManyToManyField(Projeto)

    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=100)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.nome
