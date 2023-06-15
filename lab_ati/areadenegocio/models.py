from django.db import models
from lab_ati.empresa.models import Empresa
from django.contrib.postgres.fields import ArrayField

class AreaDeNegocio(models.Model):
    id_empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        verbose_name="Empresa relacionada",
        related_name="empresa_del_area_de_negocio",
        null=True, blank=True
    )
    nombre_empresa = models.CharField("Nombre de la empresa", max_length=255)
    nombre = models.CharField("Nombre del área de negocio", max_length=255)
    pais = ArrayField(
        models.CharField("País", max_length=255),
        blank=True,
        null=True,
    )
    descripcion = models.TextField("Descripción del área de negocio", null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Áreas de Negocio"
