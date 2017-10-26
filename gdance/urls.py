from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^', include('gdance.apps.base.urls')),
	url(r'^usuario/', include('gdance.apps.users.urls')),
	url(r'^evento/', include('gdance.apps.evento.urls')),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]