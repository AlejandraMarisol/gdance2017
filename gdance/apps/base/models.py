# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

TIPO_DOCUMENTO_CHOICES = (
	('TI', 'Tarjeta de identidad'),
	('CC', 'Cédula de ciudadanía'),
)

DIA_SEMANA_CHOICES = (
	('1', 'Lunes'),
	('2', 'Martes'),
	('3', 'Miércoles'),
	('4', 'Jueves'),
	('5', 'Viernes'),
	('6', 'Sabado'),
	('7', 'Domingo'),
)

ESTADO_CHOICES = (
	('A', 'Activo'),
	('I', 'Inactivo'),
)

class Modalidad(models.Model):
	nombre_modalidad = models.CharField(max_length = 30)
	edad_minima = models.CharField(max_length = 1)
	edad_maxima = models.CharField(max_length = 1)

	def __str__(self):
		return self.nombre_modalidad

	def __unicode__(self):
		return self.nombre_modalidad

class NivelModalidad(models.Model):
	nombre_nivel = models.CharField(max_length = 20)
	modalidad = models.ForeignKey(Modalidad)

	def __str__(self):
		return self.nombre_nivel+' - '+self.modalidad.nombre_modalidad

	def __unicode__(self):
		return self.nombre_nivel+' - '+self.modalidad.nombre_modalidad