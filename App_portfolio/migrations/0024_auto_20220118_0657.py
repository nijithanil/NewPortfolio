# Generated by Django 2.2.12 on 2022-01-18 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_portfolio', '0023_services_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='services_update',
            name='Services_Quotes',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='services_update',
            name='Services_Icon',
            field=models.CharField(max_length=150),
        ),
    ]