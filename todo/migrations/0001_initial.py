# Generated by Django 4.0.5 on 2022-07-03 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_de_criacao', models.DateField(auto_now=True, verbose_name='Data da Tarefa')),
                ('tarefa', models.CharField(max_length=120, unique=True, verbose_name='Tarefa')),
                ('concluida', models.BooleanField(verbose_name='Concluído')),
            ],
            options={
                'verbose_name': 'Tarefa',
                'verbose_name_plural': 'Tarefas',
            },
        ),
    ]
