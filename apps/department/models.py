from django.db import models

class Department(models.Model):
    name = models.CharField('Name', max_length=50)
    short_name = models.CharField('Short name', max_length=20)
    active = models.BooleanField('Active', default=True)

    class Meta():
        verbose_name = 'My Deparment'
        verbose_name_plural = 'Areas of Department'
        ordering = ['id']
        unique_together = ('name', 'short_name')

    def __str__(self):
        return self.name
