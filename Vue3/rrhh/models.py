from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
        
        class Meta:
            verbose_name = "Persona"
            verbose_name_plural = "Personas"