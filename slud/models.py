from django.db import models

class Speaker(models.Model):
    nombre = models.CharField(max_length=50)
    trabajo = models.CharField(max_length=100)
    foto = models.URLField(max_length=200)

    def __str__(self):
        return self.nombre

class Charla(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=255)
    speakers = models.ManyToManyField(Speaker)
    #TODO: make date and hour fields.
    def __str__(self):
        return self.titulo
