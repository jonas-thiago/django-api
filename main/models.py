from django.db import models
import uuid

# Create your models here.

class Concessionaria(models.Model):
    SETOR_CHOICES = [
        ('oficina', 'oficina'),
        ('showroom', 'showroom'),
    ]

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        null = False,
        blank = True
    )

    codigo = models.CharField(
        max_length =8,
        null = False,
        blank = True
    )

    setor = models.CharField(
        max_length =30,
        null = False,
        blank = False,
        choices = SETOR_CHOICES
    )

    veiculo = models.CharField(
        null = False,
        blank = False,
        max_length = 50,
    )

    valor_veiculo = models.DecimalField(
        null = True,
        blank = True,
        max_digits = 8,
        decimal_places = 2
    )

    quantidade_veiculos = models.IntegerField(
        null = False,
        blank = False,
        max_length = 5
    )

    def __str__(self):
        return self.veiculo

