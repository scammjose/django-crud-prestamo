from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('equipos',views.equipos,name='equipos'),
    path('equipos/crear',views.crear,name='crear_equipo'),
    path('equipos/editar/<int:id>',views.editar, name='editar_equipo'),
    path('equipos/eliminar/<int:id>',views.borrar, name='borrar_equipo'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)