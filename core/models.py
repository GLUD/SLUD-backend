from django.db import models

class Speaker(models.Model):
    nombre = models.CharField(max_length=50)
    trabajo = models.CharField(max_length=100)
    charla = models.CharField(max_length=100)
    descripcion_charla = models.TextField(max_length=255)
    foto = models.CharField(max_length=200)
