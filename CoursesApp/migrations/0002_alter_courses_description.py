# Generated by Django 4.0 on 2021-12-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoursesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.TextField(max_length=400, verbose_name='Description'),
        ),
    ]
