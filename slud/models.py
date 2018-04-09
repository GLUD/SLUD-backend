from django.db import models

class Speaker(models.Model):
    nombre = models.CharField(max_length=100)
    trabajo = models.CharField(max_length=100, blank=True)
    foto = models.URLField(max_length=400, blank=True)
    prioridad = models.CharField(max_length=2, default="0")

    def __str__(self):
        return self.nombre

class Charla(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=255)
    speakers = models.ManyToManyField(Speaker)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(
        max_length=150,
        blank=True,
    )
    #TODO: make date and hour fields.
    def __str__(self):
        return self.titulo

class Sponsor(models.Model):
    logo = models.URLField(max_length=400)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class SpeakerRequest(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='nombre',
        null=True,
        blank=True,
    )

    email = models.CharField(
        max_length=255,
        verbose_name='correo electrónico',
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=255,
        verbose_name='titulo',
        null=True,
        blank=True,
    )

    description = models.CharField(
        max_length=255,
        verbose_name='descripción',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title or 'Posible charla {}'.format(self.id)

    class Meta:
        verbose_name = 'Posible charla'
        verbose_name_plural = 'Posibles charlas'
