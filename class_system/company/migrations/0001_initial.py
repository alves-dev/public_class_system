# Generated by Django 2.0.2 on 2020-04-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Nome')),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('contact', models.CharField(max_length=30, verbose_name='Contato')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ['name'],
            },
        ),
    ]