from django.db import models

# Create your models here.
class Tarefas(models.Model):
    STATUS_CHOICES = [
        (1,'A Fazer'),
        (2,'Fazendo'),
        (1,'Concluido'),
    ]
    titulo = models.CharField(max_length=100, null=False,blank=False)
    descrição = models.TextField(null=False,blank=False)
    data = models.DateField(null=False,blank=False)
    status = models.IntegerField(choices=STATUS_CHOICES, null=False,blank=False)