
from django.urls import include, path
from django.contrib import admin
from . import views

app_name = 'dep_app'
urlpatterns = [
   path('new_departamento/', views.NewDepartamentoView.as_view(), name='new_departamento'),
   path('lista_departamento/', views.ListaDepartamentos.as_view(), name='lista_dep'),
]