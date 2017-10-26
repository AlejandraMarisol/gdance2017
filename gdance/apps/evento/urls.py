from django.conf.urls import patterns, url, include
from .views import *

evento_detail_patterns = [
	url(r'^actualizar/$', EventoUpdateView.as_view(), name='edit-evento'),
]

urlpatterns = patterns('gdance.apps.evento.views',
	url(r'^$', EventoListView.as_view(), name = 'list-evento'),
	url(r'^agregar/$', EventoAddView.as_view(), name = 'add-evento'),
	url(r'^(?P<pk>\d+)/', include(evento_detail_patterns)),
)