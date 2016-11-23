from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [

	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),
    url(r'^$', views.CompraNueva),
    url(r'^comra/nueva/$', views.CompraNueva, name='CompraNueva'),
    ]
