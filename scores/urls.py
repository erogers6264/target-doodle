from django.conf.urls import url

from . import views

app_name = 'scores'
urlpatterns = [
    # ex: /scores/
    url(r'^$', views.index, name='index'),
    # ex: /scores/5/
    url(r'^(?P<college_id>[0-9]+)/$', views.collegeDetail, name='detail'),
    # ex: /scores/all/
    url(r'^all/$', views.allColleges, name='allColleges')
]
