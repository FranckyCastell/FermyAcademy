# Generated by Django 4.0 on 2022-01-05 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
    ]