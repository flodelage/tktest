from django.conf.urls import url
from apptkt import views

app_name = 'apptkt'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<company_id>[0-9]+)/$', views.detail, name="detail"),
]
