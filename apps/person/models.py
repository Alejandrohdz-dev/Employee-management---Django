from django.db import models
from apps.department.models import Department
from ckeditor.fields import RichTextField

class Skills(models.Model):
    skill = models.CharField('Skill', max_length=50)
    
    class Meta():
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills Employee'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + ' - ' + self.skill

class Employee(models.Model):
    
    job_choices = (
        ('0', 'Frontend'),
        ('1', 'Backend'),
        ('2', 'Full Stack'),
        ('3', 'Accounter'),
        ('4', 'Administrator'),
        ('5', 'Arquitect')
    )
 
    first_name = models.CharField('Names', blank = False, max_length=50)
    last_name = models.CharField('Last names', blank = False, max_length=50)
    full_name = models.CharField('Full name', max_length=100, blank= True)
    job = models.CharField('Job',blank = False, max_length=1, choices = job_choices)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    # life_sheet = RichTextField()
    avatar = models.ImageField(upload_to='employee',blank=True, null=True)

    class Meta():
        verbose_name = 'My Employee'
        verbose_name_plural = 'Company Employee'
        ordering = ['id']
        unique_together = ('first_name', 'department')

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + '  ' + self.last_name