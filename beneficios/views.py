from rest_framework import viewsets
from .models import BeneficiadoPorDia, Estudiante, Dia, FilaVirtual
from .serializer import BeneficiadoPorDiaSerializer, EstudianteSerializer, DiaSerializer, FilaVirtualSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

# Create your views here.
class BeneficiadoPorDiaViewSet(viewsets.ModelViewSet):
    queryset = BeneficiadoPorDia.objects.all()
    serializer_class = BeneficiadoPorDiaSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class DiaViewSet(viewsets.ModelViewSet):
    queryset = Dia.objects.all()
    serializer_class = DiaSerializer

class FilaVirtualViewSet(viewsets.ModelViewSet):
    queryset = FilaVirtual.objects.all()
    serializer_class = FilaVirtualSerializer

@api_view(['POST'])
def generar_turno(request):
    codigo = request.data.get("codigo")

    try:
        estudiante = Estudiante.objects.get(codigo_estudiantil=codigo)
    except Estudiante.DoesNotExist:
        return Response({"error": "Estudiante no encontrado o no tiene beneficio."}, status=404)

    ya_en_fila = FilaVirtual.objects.filter(estudiante=estudiante).exists()
    if ya_en_fila:
        return Response({"error": "Ya estás en la fila. Espera a ser atendido o eliminado."}, status=403)
    
    hoy = datetime.now().strftime("%A").lower()  # 'monday', 'tuesday'...
    print("Día actual (hoy):", hoy)

    try:
        dia_actual = Dia.objects.get(nombre__iexact=hoy)
        print("Día actual (objeto):", dia_actual)
        #print("Beneficio encontrado:", BeneficiadoPorDia.objects.get(estudiante=estudiante.id))
        beneficio = BeneficiadoPorDia.objects.get(estudiante=estudiante.id, dia_beneficiado=dia_actual.id)
        
    except:
        return Response({"error": "Este estudiante no puede reclamar hoy."}, status=403)

    turno = FilaVirtual.objects.create(estudiante=estudiante)
    return Response({"mensaje": "Turno generado exitosamente", "turno_id": turno.id})