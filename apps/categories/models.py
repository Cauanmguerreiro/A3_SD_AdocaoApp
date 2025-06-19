from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome")
    description = models.TextField(max_length=100, verbose_name="Descrição")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['name'] # Boa prática para ordenação padrão