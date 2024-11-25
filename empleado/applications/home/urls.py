from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.PersonaListView.as_view()),
    path('listaprueba/', views.ModeloPruebaListView.as_view()),
    
]
