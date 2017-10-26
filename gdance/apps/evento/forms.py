# -*- encoding: utf-8 -*-
from django.forms import *
from django import forms
from .models import *

class EventoForm(forms.ModelForm):

	class Meta:
		model = Evento
		fields = '__all__'
		exclude = ('organizador', )
		widgets = {
			'nombre_evento': forms.TextInput(attrs = {'class': 'form-control','required': True}),
			'direccion_evento': forms.TextInput(attrs = {'class': 'form-control','required': True}),
			'fecha_evento': forms.TextInput(attrs = {'class': 'form-control date','required': True})
		}
		labels = {
			'nombre_evento': 'Nombre del evento',
			'direccion_evento': 'Dirección del evento',
			'fecha_evento': 'Fecha del evento'
		}

	def __init__(self, *args, **kwargs):
		slug = kwargs.pop('slug', None)
		super(EventoForm, self).__init__(*args, **kwargs)
		self.fields['estado'].widget.attrs.update({'required': True, 'class': 'form-control'})

class EventSearchForm(forms.Form):
	buscar_por = forms.CharField(label = 'Buscar por:', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Digite palabra a buscar'}))

	def __init__(self, *args, **kwargs):
		buscar_por = kwargs.pop('buscar_por', None)
		super(EventSearchForm, self).__init__(*args, **kwargs)
		if buscar_por: self.fields['buscar_por'].initial = buscar_por