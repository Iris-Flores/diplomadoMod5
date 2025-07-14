from rest_framework import serializers
from .models import Taller, Estudiante, inscripcion, material


class TallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = inscripcion
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = material
        fields = '__all__'

class ReporteEstudiantesSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    estudiantes = EstudianteSerializer(many= True)