from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Courses (models.Model):
    title = models.CharField(verbose_name='Title',
                             blank=False, null=False, max_length=50)

    description = models.TextField(verbose_name='Description',
                                   blank=False, null=False, max_length=400)

    price = models.FloatField(verbose_name='Price', blank=False, null=False)

    image = models.ImageField(verbose_name='Image',
                              upload_to='Courses', null=True, blank=True)

    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)

    updated = models.DateTimeField(verbose_name='Updated', auto_now_add=True)

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.title
