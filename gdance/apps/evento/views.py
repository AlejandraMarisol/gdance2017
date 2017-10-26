# -*- encoding: utf-8 -*-
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *

template_dir = 'evento/'

class EventoListView(FormMixin, ListView):
	model = Evento
	paginate_by = 10
	form_class = EventSearchForm
	template_name = template_dir+'list_evento.html'

	def get_context_data(self, **kwargs):
		context = super(EventoListView, self).get_context_data(**kwargs)
		context['title'] = 'Lista de eventos'
		return context

	def get_form_kwargs(self):
		kwargs = super(EventoListView, self).get_form_kwargs()
		kwargs['buscar_por'] = self.request.GET.get('buscar_por')
		return kwargs

	def get_queryset(self):
		queryset = super(EventoListView, self).get_queryset()
		if self.request.GET.get('buscar_por') is not None:
			find_by = self.request.GET.get('buscar_por')
			queryset = queryset.filter(nombre_evento__icontains = find_by)
		return queryset

class EventoAddView(SuccessMessageMixin, CreateView):
	template_name = 'elements/form_general.html'
	success_message = 'Evento agregado correctamente'
	form_class = EventoForm

	def get_context_data(self, **kwargs):
		context = super(EventoAddView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar evento'
		context['url'] = reverse('add-evento')
		return context

	def form_valid(self, form):
		form.instance.organizador = self.request.user.profileuser
		return super(EventoAddView, self).form_valid(form)

	def get_success_url(self):
		return reverse('list-evento')

class EventoUpdateView(SuccessMessageMixin, UpdateView):
	model = Evento
	template_name = 'elements/form_general.html'
	success_message = 'Evento actualizado correctamente'
	form_class = EventoForm

	def get_context_data(self, **kwargs):
		context = super(EventoUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Actualizar evento'
		context['url'] = reverse('edit-evento', kwargs = {'pk': self.kwargs['pk']})
		return context

	def get_success_url(self):
		return reverse('list-evento')