from django.conf.urls import patterns, url

from scans import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add', views.add, name='add'),
    url(r'^(?P<scan_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<scan_id>\d+)/run/$', views.extract_to_files, name='extract_to_files'),
    url(r'^(?P<scan_id>\d+)/files/$', views.files, name='files'),
    url(r'^(?P<scan_id>\d+)/files/(?P<file_id>\d+)$', views.file_result, name='file_result'),
    
)
