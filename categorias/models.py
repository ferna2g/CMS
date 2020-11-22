from django.db import models

# Create your models here.
class Categories(models.Model):
    categoria = models.CharField(max_length = 40)

    def __str__(self):
        return self.categoria
