# Generated by Django 2.2.12 on 2022-01-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_portfolio', '0025_myteam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myteam',
            name='Position',
            field=models.CharField(max_length=150),
        ),
    ]
