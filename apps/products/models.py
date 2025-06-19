from django.db import models
from categories.models import Category # <-- Adicione esta linha para importar Category

class Product(models.Model): # <-- Defina a classe Product
    name = models.CharField(max_length=100, verbose_name="Nome do Produto")
    description = models.TextField(verbose_name="Descrição")
    date_fabrication = models.DateField(verbose_name="Data de Fabricação")
    is_active = models.BooleanField(default=True, verbose_name="Ativo")
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT, # Ou models.SET_NULL, models.CASCADE dependendo da regra de negócio
        null=True, # <-- Estes parâmetros devem estar dentro da chamada ForeignKey
        blank=True, # <-- Estes parâmetros devem estar dentro da chamada ForeignKey
        verbose_name="Categoria"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['name']
