# Generated by Django 2.2 on 2020-04-10 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.Endereco'),
        ),
    ]