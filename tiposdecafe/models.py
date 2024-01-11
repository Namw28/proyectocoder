from django.db import models

class Granos(models.Model):
    nombre = models.CharField(max_length=100)
    region_produccion = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30)
    altura_cultivo = models.DecimalField(max_digits=5, decimal_places=2, default= 0)
    tipo_semillas = models.CharField(max_length=50, default= 0)
    tiempo_cosecha = models.CharField(max_length=50, default= 0)
    

    def __str__(self):
        return f"{self.nombre} - Tipo: {self.tipo} - Se produce en: {self.region_produccion}"

class Origenes(models.Model):
    pais = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.pais} - Región: {self.region}"

class Tostado(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} - Nivel: {self.nivel}"

class Preparacion(models.Model):
    nombre = models.CharField(max_length=100)
    metodo = models.CharField(max_length=30)  
    tiempo = models.DecimalField(max_digits=2, decimal_places=2)
    temperatura = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return f"{self.nombre} - Método: {self.metodo}"





""" la idea es crear especificaiones de los distintos granos altura, tipo de semilla, tiempo de cosecha, origen+historia"""


"""especie, tipo, zona_de_cosecha, pais_de_origen, metodo_de_procesamiento, altitud_de_cultivo"""