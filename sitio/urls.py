from django.conf.urls import include, url
from django.contrib.auth import views
import django.contrib.auth.views
from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('ventas.urls')),
]
