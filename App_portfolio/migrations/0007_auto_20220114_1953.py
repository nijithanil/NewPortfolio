# Generated by Django 2.2.12 on 2022-01-14 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_portfolio', '0006_auto_20220114_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_update',
            name='Phone',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
