from django.db import models
from apps.clients.models import Client # Ajustado o caminho do import

# Create your models here.
class Order(models.Model):
    PAYMENT_METHOD_CHOICES = [ # Definido como uma variável de classe para melhor organização
        ('boleto', 'Boleto'),
        ('cartao', 'Cartão de Crédito'),
        ('pix', 'PIX'),
    ]
    STATUS_CHOICES = [ # Definido como uma variável de classe para melhor organização
        ('andamento', 'Em andamento'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]

    payment_method = models.CharField('Forma de Pagamento', max_length=30, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField('Status', max_length=20, default='andamento', choices=STATUS_CHOICES)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Cliente") # Adicionado verbose_name
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering =['id']

    def __str__(self):
        return f"Pedido {self.id} - {self.client}" # Melhor representação __str__