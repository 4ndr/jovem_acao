from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mostra_mvv ,name='mostra_mvv'),
]