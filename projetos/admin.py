from django.contrib import admin
from .models import Projetos

# Register your models here.

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'icone']
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Projetos, ProjetoAdmin)