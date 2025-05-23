from django.urls import path, include
from rest_framework import routers
from beneficios.views import BeneficiadoPorDiaViewSet, EstudianteViewSet, FilaVirtualViewSet, generar_turno

router = routers.DefaultRouter()
router.register(r"beneficiado_dia", BeneficiadoPorDiaViewSet)
router.register(r"estudiante", EstudianteViewSet)
router.register(r"fila_virtual", FilaVirtualViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/generar_turno/", generar_turno, name="generar_turno"),
]