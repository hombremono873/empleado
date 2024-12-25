
from django.urls import include, path
from django.contrib import admin
from . import views
 
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('new_departamento/', views.NewDepartamentoView.as_view(), name='new_departamento'),
]