from django import forms

class CityForm(forms.Form):
    city = forms.ChoiceField(
        choices=[
            ('1110600', 'Lisboa'),
            ('1101400', 'Porto'),
            ('1050200', 'Coimbra'),
            # Adicione outras cidades conforme necessário
        ],
        label='Escolha a cidade'
    )