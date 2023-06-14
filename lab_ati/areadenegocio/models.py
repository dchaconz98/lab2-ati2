from django.db import models
from lab_ati.empresa.models import Empresa

class AreaDeNegocio(models.Model):
    id_empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        verbose_name="Empresa relacionada",
        related_name="areas_de_negocio"
    )
    nombre_empresa = models.CharField("Nombre de la empresa", max_length=255)
    nombre = models.CharField("Nombre del área de negocio", max_length=255)
    paises = models.ManyToManyField(
        "Pais",
        verbose_name="Países",
        related_name="areas_de_negocio"
    )
    descripcion = models.TextField("Descripción del área de negocio")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Áreas de Negocio"


class Pais(models.Model):
    nombre = models.CharField("Nombre del país", max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Países"