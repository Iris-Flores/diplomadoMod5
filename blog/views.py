from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view

from .forms import EstudianteForm
from .models import Estudiante, Taller, inscripcion, material
from .serializers import ReporteEstudiantesSerializer, TallerSerializer, EstudianteSerializer, MaterialSerializer, InscripcionSerializer

def index(request):
    return HttpResponse ("hola Mundo")

def contact(request, name):
    return HttpResponse (f"Bienvenido {name}")

def talleres(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Taller(nombre=post_nombre)
        q.save()
    filtro_nombre = request.GET.get('nombre')
    if filtro_nombre:
        talleres = Taller.objects.filter(nombre__contains = filtro_nombre)
    else:
        talleres = Taller.objects.all()

        
    return render(request, 'form_talleres.html',{
        "talleres": talleres
    })

def estudianteFormView(request):
    form = EstudianteForm()
    estudiante = None

    id_estudiante = request.GET.get('id')
    if id_estudiante:
        estudiante = get_object_or_404(Estudiante, id=id_estudiante)
        form = EstudianteForm(instance=estudiante)
    if request.method == 'POST':
        if estudiante:
            form = EstudianteForm(request.POST, instance=estudiante)
        else:
            form = EstudianteForm(request.POST)

    if form.is_valid():
        form.save()
    return render(request, 'form_estudiantes.html',{
        "form": form
    })



class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = inscripcion.objects.all()
    serializer_class = InscripcionSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = material.objects.all()
    serializer_class = MaterialSerializer


#---
class TallerCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer

class EstudianteCreateView(generics.CreateAPIView, generics.ListAPIView, generics.RetrieveUpdateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class InscripcionCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = inscripcion.objects.all()
    serializer_class = InscripcionSerializer

class MaterialCreateView(generics.CreateAPIView, generics.ListAPIView, generics.RetrieveUpdateAPIView):
    queryset = material.objects.all()
    serializer_class = MaterialSerializer

@api_view(['GET'])
def Estudiante_count(request):
    try:
        cantidad = Estudiante.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe= False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)
    


@api_view (['GET'])
def estudiantes_en_taller (request):
    try:
        estudiantes = Estudiante.objects.filter(nivel='intermedio')
        return JsonResponse(
        EstudianteSerializer(estudiantes, many=True).data,
        safe=False,
        status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)
    
@api_view(['GET'])
def reporte_estudiantes(request):
    try:
        estudiantes = Estudiante.objects.filter(edad__lt=18)
        cantidad = estudiantes.count()
        return JsonResponse(
            ReporteEstudiantesSerializer({
                "cantidad": cantidad,
                "estudiantes": estudiantes,
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)

