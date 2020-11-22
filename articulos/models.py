from django.db import models

from django.contrib.auth.models import User
from categorias.models import Categories

# Create your models here.
class Articles(models.Model):
    titulo = models.CharField(max_length = 50)
    resumen = models.CharField(max_length = 50)
    contenido = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(null=False, blank=False, unique=True)
    portada = models.CharField(max_length = 50)
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categories, on_delete=models.CASCADE)
