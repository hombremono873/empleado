from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view(), name='home'),  # Agrega el nombre de la ruta
    path('lista/', views.PersonaListView.as_view(), name='lista'),
    path('listaprueba/', views.ModeloPruebaListView.as_view(), name='listaprueba'),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),  # Nombre para la vista de creación de pruebas
    path('resumen_foundatium/', views.ResumeFoundatiumView.as_view(), name='resumenfoundatium'),
]
