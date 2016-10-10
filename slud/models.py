from django.db import models

class Speaker(models.Model):
    nombre = models.CharField(max_length=100)
    trabajo = models.CharField(max_length=100, blank=True)
    foto = models.URLField(max_length=400, blank=True)

    def __str__(self):
        return self.nombre

class Charla(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=255)
    speakers = models.ManyToManyField(Speaker)
    fecha = models.DateField()
    hora = models.TimeField()
    #TODO: make date and hour fields.
    def __str__(self):
        return self.titulo

class Sponsor(models.Model):
    logo = models.URLField(max_length=400)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
