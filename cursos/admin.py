from django.contrib import admin
from .models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente

# Register your models here.
admin.site.register(Curso)
admin.site.register(AreaCientifica)
admin.site.register(Disciplina)
admin.site.register(Projeto)
admin.site.register(LinguagemProgramacao)
admin.site.register(Docente)