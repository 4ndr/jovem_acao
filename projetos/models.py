from django.db import models

# Create your models here.

class Projetos(models.Model):
    nome = models.CharField('titulo', max_length=200)
    slug = models.SlugField("Atalho", max_length=200, unique=True, blank=True)
    descricao = models.TextField('descricao', null=True)
    icone = models.ImageField(upload_to='projetos')
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    def __str__(self):
        return self.nome

    @models.permalink
    def get_absolute_url(self):
        return 'projetos:nome', (), {'slug': self.slug}

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'


# class Acoes(models.Model):