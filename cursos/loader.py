import os
import json


from django.db import transaction
from cursos.models import Curso, Disciplina, AreaCientifica

Curso.objects.all().delete()
Disciplina.objects.all().delete()
AreaCientifica.objects.all().delete()

def importar_curso(nome_arquivo):
    try:

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_json = os.path.join(diretorio_atual, nome_arquivo)

        with open(caminho_json, 'r') as arquivo:
            dados_curso = json.load(arquivo)

            with transaction.atomic():

                detalhes_curso = dados_curso['courseDetail']
                curso, created = Curso.objects.get_or_create(
                    nome=detalhes_curso['courseName'],
                    apresentacao=detalhes_curso['presentation'],
                    objetivos=detalhes_curso['objectives'],
                    competencias=detalhes_curso['competences']
                )


                for disciplina_data in dados_curso['courseFlatPlan']:
                    area_cientifica, _ = AreaCientifica.objects.get_or_create(
                        nome=detalhes_curso['scientificArea']
                    )
                    disciplina, created = Disciplina.objects.get_or_create(
                        nome=disciplina_data['curricularUnitName'],
                        ano=disciplina_data['curricularYear'],
                        semestre=disciplina_data['semester'],
                        ects=disciplina_data['ects'],
                        curricularIUnitCode=disciplina_data['curricularIUnitReadableCode'],
                        areaCientifica=area_cientifica,
                        curso=curso
                    )

        print("Importação concluída com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro durante a importação: {e}")

