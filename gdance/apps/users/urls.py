from django.contrib.auth.decorators import user_passes_test, permission_required, login_required
from django.conf.urls import patterns, url, include
from django.contrib.auth import views as auth_views
from .views import *

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), '/')

urlpatterns = patterns('gdance.apps.users.views',
	url(r'^ingresar/$', login_forbidden(auth_views.login), {'template_name': 'users/form_login.html', 'extra_context': {'title': 'Ingresar'}}, name = 'login'),
	url(r'^salir/$', auth_views.logout, {'next_page': '/'}, name = 'logout'),
	url(r'^(?P<tipo>[-\w]+)/$', ListUserView.as_view(), name = 'list-user'),
	url(r'^crear/(?P<tipo>[-\w]+)/$', NewUserView.as_view(), name = 'new-user'),
)