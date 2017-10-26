# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from gdance.apps.base.models import *
from django.db import models

class ProfileUser(models.Model):
	user = models.OneToOneField(User, primary_key = True)
	foto = models.ImageField(upload_to = 'img/users/', blank = True, null = True)
	tipo_documento = models.CharField(max_length = 2, choices = TIPO_DOCUMENTO_CHOICES)
	numero_documento = models.CharField(max_length = 10)
	numero_telefono = models.CharField(max_length = 10, default = '-')
	direccion_residencia = models.CharField(max_length = 80)
	descripcion_persona = models.CharField(max_length = 2000, blank = True, null = True)

	def __str__(self):
		return str(self.user)

	def get_foto(self):
		if self.foto and hasattr(self.foto, 'url'):
			url_image = self.foto.url
		else:
			url_image = '/static/img/users/none.png'
		return url_image

	def get_tipo_documento(self):
		tipo_documento = dict(TIPO_DOCUMENTO_CHOICES)
		return tipo_documento[self.tipo_documento]

	def get_tipo_role(self):
		tipo_role = dict(TIPO_ROLE_CHOICES)
		return tipo_role[self.tipo_role]

	def get_full_name(self):
		return self.user.first_name+" "+self.user.last_name

class Schedule(models.Model):
	entrenador = models.ForeignKey(ProfileUser)
	dia_semana = models.CharField(max_length = 1, choices = DIA_SEMANA_CHOICES)
	hora_inicio = models.TimeField(auto_now = False)
	hora_final = models.TimeField(auto_now = False)

	def __str__(self):
		return self.entrenador.user.first_name

	def __unicode__(self):
		return self.entrenador.user.first_name

	def get_dia_semana(self):
		dia_semana = dict(DIA_SEMANA_CHOICES)
		return dia_semana[self.dia_semana]

class ModalidadPersona(models.Model):
	modalidad = models.ForeignKey(Modalidad)
	nivel = models.ForeignKey(NivelModalidad)
	deportista = models.ForeignKey(ProfileUser)
	fecha_ingreso = models.DateField(auto_now = False)
	estado = models.CharField(max_length = 1, choices = ESTADO_CHOICES)

	def __str__(self):
		return self.deportista.user.first_name+'-'+self.nivel.nombre_nivel

	def __unicode__(self):
		return self.deportista.user.first_name+'-'+self.nivel.nombre_nivel

	def get_estado(self):
		estado = dict(ESTADO_CHOICES)
		return estado[self.estado]