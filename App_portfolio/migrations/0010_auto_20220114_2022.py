# Generated by Django 2.2.12 on 2022-01-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_portfolio', '0009_skills_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills_update',
            old_name='Name',
            new_name='Name1',
        ),
        migrations.RenameField(
            model_name='skills_update',
            old_name='percentage',
            new_name='Percentage1',
        ),
        migrations.AddField(
            model_name='skills_update',
            name='Name2',
            field=models.CharField(default=2, max_length=150, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills_update',
            name='Percentage2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
