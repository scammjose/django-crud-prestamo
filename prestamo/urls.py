from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('prestamo',views.prestamo,name='prestamo'),
    path('prestamo/prestar',views.prestar,name='prestar_equipo'),
    path('prestamo/quitar/<int:id>',views.quitar, name='quitar_prestamo'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)