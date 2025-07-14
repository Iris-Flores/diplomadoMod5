from django.contrib import admin

# Register your models here.

from.models import Taller
from.models import Estudiante
from.models import inscripcion

admin.site.register(Taller)

admin.site.register(inscripcion)

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "edad", "nivel",)
    ordering = ["edad"]
    search_fields = ["nivel"]
    list_filter = ["nivel"]

admin.site.register(Estudiante, EstudianteAdmin)
