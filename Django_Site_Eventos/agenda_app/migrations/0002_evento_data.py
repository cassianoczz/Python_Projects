# Generated by Django 4.1.3 on 2022-11-16 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='data',
            field=models.DateField(null=True),
        ),
    ]