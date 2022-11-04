from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('laboratorios',views.laboratorios,name='laboratorios'),
    path('laboratorios/crear',views.crear,name='crear_lab'),
    path('laboratorios/editar/<int:id>',views.editar, name='editar_lab'),
    path('laboratorios/borrar/<int:id>',views.borrar, name='quitar_lab'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)