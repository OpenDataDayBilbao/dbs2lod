from django.db import models

# Create your models here.

class Pregunta(models.Model):
    enunciado = models.CharField(max_length=500)
    clave = models.CharField(max_length=10)
    
class Caso(models.Model):
    key = models.CharField(max_length=200)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    HOMBRE = 'H'
    MUJER = 'M'
    SEXO_CHOICES = (
        (HOMBRE, 'Hombre'), 
        (MUJER, 'Mujer'),
    )
    sexo = models.CharField(max_length=2, choices=SEXO_CHOICES)
    edad = models.IntegerField()
    _18_24 = '18_24'
    _25_34 = '25_34'
    _35_44 = '35_44'
    _45_54 = '45_54'
    _55_MAS = '55_MAS'
    EDAD_CHOICES = (
        (_18_24, '18-24'),
        (_25_34, '25-34'),
        (_35_44, '35-44'),
        (_45_54, '45-54'),
        (_55_MAS, '+55'),
    )
    edad_reco = models.CharField(max_length=2, choices=EDAD_CHOICES)
    ALTA = 'ALTA'
    MEDIA_ALTA = 'MEDIA_ALTA'
    MEDIA_MEDIA = 'MEDIA_MEDIA'
    MEDIA_BAJA = 'MEDIA_BAJA'
    BAJA = 'BAJA'
    NO_DEFINIDA = 'NO_DEFINIDA'
    CLASE_CHOICES = (
        (ALTA, 'Alta'),
        (MEDIA_ALTA, 'Media-Alta'),
        (MEDIA_MEDIA, 'Media-Media'),
        (MEDIA_BAJA, 'Media-Baja'),
        (BAJA, 'Baja'),
        (NO_DEFINIDA, 'No definida'), # O sea, lumpen
    )
    clase_social = models.CharField(max_length=2, choices=CLASE_CHOICES)
    provincia = models.CharField(max_length=20)
    EUSKERA = 'EUSKERA'
    CASTELLANO = 'CASTELLANO'
    IDIOMA_CHOICES = (
        (EUSKERA, 'Euskera'),
        (CASTELLANO, 'Castellano'),
    )
    idioma = models.CharField(max_length=2, choices=IDIOMA_CHOICES)
    preguntas = models.ManyToManyField(Pregunta, through='Respuesta')
    
class Respuesta(models.Model):
    caso = models.ForeignKey(Caso)
    pregunta = models.ForeignKey(Pregunta)
    respuesta = models.CharField(max_length=100)
