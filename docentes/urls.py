from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.redireccion,name='redireccion'),
    path('inicio',views.inicio,name='inicio'),
    path('docentes',views.docentes,name='docentes'),
    path('docentes/crear',views.crear,name='crear'),
    path('docentes/editar/<int:id>',views.editar, name='editar'),
    path('docentes/eliminar/<int:id>',views.borrar, name='borrar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)