# Generated by Django 4.1.3 on 2022-11-19 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=256)),
                ('data_horario', models.DateField()),
                ('telefone_cliente', models.CharField(max_length=14)),
                ('email_cliente', models.EmailField(max_length=254)),
            ],
        ),
    ]
