from django.shortcuts import render
from django.http import Http404
from .models import Projetos

# Create your views here.

def mostra_projetos(request):
    try:
        projetos = Projetos.objects.all()
    except Projetos.DoesNotExist:
        raise Http404("Não há projetos cadastrados")
    template_name = "projetos.html"
    context = {
        'projetos': projetos
    }
    return render(request, template_name, context)

def mostra_projeto(request, slug=None):
    projeto = Projetos.objects.get(slug=slug)
    template_name = "projeto.html"
    context = {
        'projeto': projeto
    }
    return render(request, template_name, context)