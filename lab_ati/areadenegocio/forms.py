from django import forms
from lab_ati.areadenegocio.models import AreaDeNegocio
from lab_ati.empresa.models import Empresa

class AreaDeNegocioForm(forms.ModelForm):

    id_empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        label="Empresa relacionada",
        to_field_name="id",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["id_empresa"].label_from_instance = self.label_from_instance

    def label_from_instance(self, obj):
        return f"{obj.id} - {obj.nombre}"

    class Meta:
        model = AreaDeNegocio
        fields = ['nombre', 'pais', 'descripcion', 'id_empresa']