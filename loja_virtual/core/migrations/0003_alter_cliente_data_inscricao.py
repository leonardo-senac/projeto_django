# Generated by Django 4.2.2 on 2023-06-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_endereco_cliente_cliente_endereco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_inscricao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]