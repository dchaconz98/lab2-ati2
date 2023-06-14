from django.urls import path
from lab_ati.areadenegocio.views import areasdenegocio, crear_areadenegocio, editar_areadenegocio, eliminar_areadenegocio, ver_areadenegocio


urlpatterns = [
    path('<slug:business_id>/areasdenegocio/', areasdenegocio, name='areasdenegocio'),
    path('<slug:business_id>/areasdenegocio/create', crear_areadenegocio, name='create-areasdenegocio'),
    path('<slug:business_id>/clients/<slug:id>', ver_areadenegocio, name='detail-areasdenegocio'),
    path('<slug:business_id>/clients/delete/<slug:id>', eliminar_areadenegocio, name='delete-areasdenegocio'),
    path('<slug:business_id>/clients/edit/<slug:id>', editar_areadenegocio, name='edit-areasdenegocio')
]