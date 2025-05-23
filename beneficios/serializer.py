from rest_framework import serializers
from .models import BeneficiadoPorDia, Estudiante, Dia, FilaVirtual

# Serializers define the API representation.
class BeneficiadoPorDiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeneficiadoPorDia
        fields = '__all__'

class DiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dia
        fields = '__all__'

class FilaVirtualSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilaVirtual
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'
