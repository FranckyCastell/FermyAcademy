from django.db import models
from django.contrib.auth.models import User
from CoursesApp.models import Courses

# Create your models here.


class Profile (models.Model):
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuario')

    cursos = models.ForeignKey(
        Courses, on_delete=models.CASCADE, verbose_name='Curso')

    pdf = models.FileField(
        verbose_name='PDF', upload_to='PDFs', null=True, blank=True)

    description = models.TextField(verbose_name='Descripción', null=True, blank=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'