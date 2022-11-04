from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('prestamo_lab',views.prestamo_lab,name='prestamo_lab'),
    path('prestamo_lab/prestar',views.prestar_lab,name='prestar_lab'),
    path('prestamo_lab/quitar/<int:id>',views.quitar_lab, name='quitar_prestamo_lab'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)