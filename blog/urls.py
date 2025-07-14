from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r"Talleres", views.TallerViewSet)
router.register(r"Estudiantes", views.EstudianteViewSet)
router.register(r"Inscripciones", views.InscripcionViewSet)
router.register(r"Materiales", views.MaterialViewSet)

urlpatterns = [
    #path('contact/<str:name>', views.contact, name='contact'),
    #path('talleres', views.talleres, name='talleres'),
    #path('estudiantes', views.estudianteFormView, name='estudiantes'),
    #path('', views.index, name='index'),
    
    path('taller', views.TallerCreateView.as_view()),
    path('estudiante', views.EstudianteCreateView.as_view()),
    #path('inscripcion', views.InscripcionCreateView.as_view()),
    #path('material', views.MaterialCreateView.as_view()),
    path('estudiante/cantidad/', views.Estudiante_count, name='estudiantes_count'),
    path('estudiante/filtrar/nivel/', views.estudiantes_en_taller, name='filtrar_nivel'),
    path('estudiante/reporte', views.estudiantes_en_taller, name='reporte_de_estudoantes_por_edad_menor'),
    path('', include(router.urls)),
]