from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mostra_projetos ,name='projetos'),
    url(r'^(?P<slug>[\w_-]+)/$', views.mostra_projeto ,name='projeto_completo'),
]