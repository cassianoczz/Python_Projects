# Generated by Django 4.1 on 2022-08-26 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=11)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anuncios_app.categoria')),
            ],
        ),
    ]
