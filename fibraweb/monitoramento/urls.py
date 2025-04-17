from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nova/', views.nova_medicao, name='nova_medicao'),
    path('lista/', views.lista_medicoes, name='lista_medicoes'),
    path('editar/<int:pk>/', views.editar_medicao, name='editar_medicao'),
    path('deletar/<int:pk>/', views.deletar_medicao, name='deletar_medicao'),

]