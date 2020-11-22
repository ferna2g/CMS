from django.db import models

from django.contrib.auth.models import User
from articulos.models import Articles

# Create your models here.
class Comments(models.Model):
    comentario = models.TextField()
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_articulo = models.ForeignKey(Articles, on_delete=models.CASCADE)
