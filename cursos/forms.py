from django import forms
from .models import Curso, Disciplina, Projeto, Docente, LinguagemProgramacao, AreaCientifica


class cursoForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields = '__all__'

    widgets = {
      'nome': forms.TextInput(attrs={
          'placeholder':'Nome do Curso',

      })
    }

    labels = {
        'nome': 'Nome do Curso',
        'apresentacao': 'Apresentação sobre o Curso',
        'objetivos': 'Objetivos do Curso',
        'competencias': 'Competencias do Curso',
        'disciplinas': 'Disciplinas do Curso',
    }

    help_texts = {

        }

class disciplinaForm(forms.ModelForm):
  class Meta:
    model = Disciplina
    fields = '__all__'

    widgets = {
      'nome': forms.TextInput(attrs={
          'placeholder':'Nome da disciplina',
      })
    }

    labels = {
      'nome': 'Nome',
      'ano': 'Ano',
      'semestre': 'Semestre',
      'ects': 'Créditos',
      'curricularIUnitCode': 'Codigo Curricular',
      'areaCientifica': 'Area Cientifica',
      'curso': 'Curso',
    }

    help_texts = {

        }

class projetoForm(forms.ModelForm):
  class Meta:
    model = Projeto
    fields = '__all__'

    widgets = {
      'title': forms.TextInput(attrs={
          'placeholder':'Título da música',
      })
    }

    labels = {
      'nome': 'Nome do Projeto',
      'descricao': 'Descrição',
      'conceitosAplicados': 'Conceitos Aplicados',
      'tecnologiasUsadas': 'Tecnologias Usadas',
      'disciplina': 'Disciplina',
    }

    help_texts = {

        }


class linguagemProgramacaoForm(forms.ModelForm):
  class Meta:
    model = LinguagemProgramacao
    fields = '__all__'

    widgets = {
      'nome': forms.TextInput(attrs={
          'placeholder':'Nome da linguagem',
      })
    }

    labels = {
      'nome': 'Nome da linguagem',
    }

    help_texts = {

        }


class docenteForm(forms.ModelForm):
  class Meta:
    model = Docente
    fields = '__all__'

    widgets = {
      'nome': forms.TextInput(attrs={
          'placeholder':'Nome do docente',
      })
    }

    labels = {
      'nome': 'Nome do Docente',
    }

    help_texts = {

        }


class areaCientificaForm(forms.ModelForm):
  class Meta:
    model = AreaCientifica
    fields = '__all__'

    widgets = {
      'nome': forms.TextInput(attrs={
          'placeholder':'Nome da área cienfífica',
      })
    }

    labels = {
      'nome': 'Nome da área cienfífica',
    }

    help_texts = {

        }