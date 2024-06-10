from django import forms
from .models import Author, Article, Comment, Rating


class authorForm(forms.ModelForm):
  class Meta:
    model = Author
    fields = '__all__'

    widgets = {
      'name': forms.TextInput(attrs={
          'placeholder':'Nome do autor',
      })
    }

    labels = {
        'name': 'Nome',
        'bio': 'Biografia',
    }

    help_texts = {
        'name': 'Insira o nome da autor.',
        'bio': 'Insira a biografia do autor.',

    }

class articleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = '__all__'

    widgets = {
      'title': forms.TextInput(attrs={
          'placeholder':'Título do artigo',
      })
    }

    labels = {
        'title': 'Título do artigo',
        'content': 'Conteúdo do artigo',

    }

    help_texts = {
            'title': 'Insira o título do artigo.',
        }

class commentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = '__all__'


class ratingForm(forms.ModelForm):
  class Meta:
    model = Rating
    fields = '__all__'

