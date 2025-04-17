from django.db import models


class Fibra(models.Model):
    CLIENTE_CHOICES = [
        ('FTTH', 'Fibra até a casa'),
        ('FTTC', 'Fibra até o armário'),
        ('FTTB', 'Fibra até o prédio'),
    ]

    nome_cliente = models.CharField(max_length=100)
    tipo_fibra = models.CharField(max_length=4, choices=CLIENTE_CHOICES)
    nivel_sinal = models.FloatField()
    data_medicao = models.DateTimeField(auto_now_add=True)

    # Novos campos de endereço
    rua = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    cep = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return f"{self.nome_cliente} - {self.tipo_fibra}"



