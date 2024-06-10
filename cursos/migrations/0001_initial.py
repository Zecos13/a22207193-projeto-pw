# Generated by Django 4.0.6 on 2024-06-05 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCientifica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('apresentacao', models.TextField()),
                ('objetivos', models.TextField()),
                ('competencias', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('semestre', models.CharField(max_length=20)),
                ('ects', models.IntegerField()),
                ('curricularIUnitCode', models.CharField(max_length=100)),
                ('areaCientifica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.areacientifica')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('conceitosAplicados', models.TextField()),
                ('tecnologiasUsadas', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='projeto_images')),
                ('linkVideo', models.URLField(blank=True, null=True)),
                ('linkGithub', models.URLField(blank=True, null=True)),
                ('disciplina', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cursos.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='LinguagemProgramacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('projetos', models.ManyToManyField(to='cursos.projeto')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('disciplinas', models.ManyToManyField(to='cursos.disciplina')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='disciplinas',
            field=models.ManyToManyField(related_name='cursos', to='cursos.disciplina'),
        ),
    ]
