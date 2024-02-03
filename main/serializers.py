from rest_framework import serializers
from .models import Concessionaria

class ConcessionariaSerializer(serializers.ModelSerializer):
    '''Essa classe estar responsável por serializar e desserializar as informações'''
    class Meta:
        model = Concessionaria
        fields = [
            'id',
            'codigo',
            'setor',
            'veiculo',
            'valor_veiculo',
            'quantidade_veiculos',
        ]