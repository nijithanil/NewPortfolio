# Generated by Django 2.2.12 on 2022-01-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_portfolio', '0030_auto_20220118_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='Link',
            field=models.CharField(default=1, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
