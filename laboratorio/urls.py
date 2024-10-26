from django.urls import path
from . import views
urlpatterns = [
    path('', views.insertar_lab, name='insertar-lab'),
    path('mostrar/', views.mostrar_lab, name='mostrar-lab'),
    path('editar/<int:pk>', views.editar_lab, name='editar-lab'),
    path('editar/actualizarlaboratorio/<int:pk>', views.actualizar_lab, name='actualizarlaboratorio'),
    path('eliminar/<int:pk>/', views.eliminar_lab, name='eliminar-lab'),
    path("inicio/", views.InicioPageView.as_view(), name="inicio"),
    path("acerca-de/", views.AcercaPageView.as_view(), name="acerca-de"),
]

