# Generated by Django 4.0.5 on 2022-07-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todomodel_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='autor',
            field=models.CharField(max_length=120, unique=True, verbose_name='Autor'),
        ),
    ]
