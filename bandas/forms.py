from django import forms
from .models import Band, Album, Song


class bandForm(forms.ModelForm):
  class Meta:
    model = Band
    fields = '__all__'

    widgets = {
      'name': forms.TextInput(attrs={
          'placeholder':'Nome da banda',
      })
    }

    labels = {
      'name': 'Nome da Banda',
      'photo': 'Foto',
      'biography': 'Biografia',
      'yearFormation': 'Ano de formação',
      'genre': 'Genero'
    }

    help_texts = {
            'name': 'Insira o nome da banda.',
            'photo': 'Carregue uma foto da banda.',
            'info': 'Insira informações da banda.',
            'biography': 'Insira a biografia da banda.',
            'yearFormation': 'Insira o ano de formação da banda.',
            'genre': 'Insira o gênero musical da banda.'
        }

class albumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = '__all__'

    widgets = {
      'title': forms.TextInput(attrs={
          'placeholder':'Título do álbum',
      })
    }

    labels = {
      'title': 'Título do Álbum',
      'releaseDate': 'Ano de Lançamento',
      'band': 'Banda',
      'cover': 'Capa',
    }

    help_texts = {
            'title': 'Insira o título do álbum.',
            'band': 'Insira a banda que tem este álbum.',
            'cover': 'Carregue uma imagem do álbum.',
            'releaseDate': 'Insira a data de lançamento do álbum.',
            'label': 'Insira a label que lançou este álbum.'
        }

class songForm(forms.ModelForm):
  class Meta:
    model = Song
    fields = '__all__'

    widgets = {
      'title': forms.TextInput(attrs={
          'placeholder':'Título da música',
      })
    }

    labels = {
      'title': 'Título da Música',
      'lyrics': 'Letra',
      'duration': 'Duração',
      'linkSpotify': 'Link Spotify',
    }

    help_texts = {
            'title': 'Insira o título da música.',
            'album': 'Insira o àlbum que tem esta música.',
            'linkSpotify': 'Insira o link Spotify da música.',
            'lyrics': 'Insira a letra da música, se houver.',
            'duration': 'Insira a duração da música.',
        }