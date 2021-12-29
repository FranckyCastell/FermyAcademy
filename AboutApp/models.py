from django.db import models

# Create your models here.


class Users (models.Model):
    name = models.CharField(verbose_name='Name',
                            blank=False, null=False, max_length=50)

    image = models.ImageField(verbose_name='Image',
                              upload_to='Personal', null=True, blank=True)

    description = models.CharField(verbose_name='Description',
                                   blank=False, null=False, max_length=300)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.name
