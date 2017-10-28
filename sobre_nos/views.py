from django.shortcuts import render
from django.http import Http404
from .models import SobreNos

# Create your views here.

def mostra_mvv(request):
    try:
        mvv = SobreNos.objects.all()
    except SobreNos.DoesNotExist:
        raise Http404("Sobre nós não existe")
    template_name = 'sobre_nos.html'
    context = {
        'missao': mvv[0].missao,
        'visao': mvv[0].visao,
        'valores': mvv[0].valores,
    }

    return render(request, template_name, context)