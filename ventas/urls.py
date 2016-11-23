from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CompraNueva),
    url(r'^comra/nueva/$', views.CompraNueva, name='CompraNueva'),
    ]
