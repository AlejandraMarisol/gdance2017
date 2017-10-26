from django.contrib.auth.decorators import permission_required
from django.conf.urls import patterns, url, include
from .views import *

urlpatterns = patterns('socialapp.apps.home.views',
	url(r'^$', InicioTemplateView.as_view(), name = 'inicio'),
	url(r'^nosotros/$', NosotrosTemplateView.as_view(), name = 'nosotros'),
)