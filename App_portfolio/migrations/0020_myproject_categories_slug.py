# Generated by Django 2.2.12 on 2022-01-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_portfolio', '0019_auto_20220117_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproject_categories',
            name='slug',
            field=models.SlugField(default=1, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
