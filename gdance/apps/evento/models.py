# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from gdance.apps.users.models import *
from gdance.apps.base.models import *
from django.db import models

class Evento(models.Model):
	nombre_evento = models.CharField(max_length = 45)
	direccion_evento = models.CharField(max_length = 80)
	fecha_evento = models.DateTimeField(auto_now = False)
	estado = models.CharField(max_length = 1, choices = ESTADO_CHOICES)
	organizador = models.ForeignKey(ProfileUser)

	def __str__(self):
		return self.nombre_evento

	def __unicode__(self):
		return self.nombre_evento

	def get_estado(self):
		estado = dict(ESTADO_CHOICES)
		return estado[self.estado]