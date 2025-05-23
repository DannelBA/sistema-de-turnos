from django.contrib import admin
from .models import Estudiante, Dia, BeneficiadoPorDia, FilaVirtual
# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Dia)
admin.site.register(BeneficiadoPorDia)
admin.site.register(FilaVirtual)