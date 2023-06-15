from django import forms
from lab_ati.areadenegocio.models import AreaDeNegocio
from lab_ati.empresa.models import Empresa
from django_countries import countries

class AreaDeNegocioForm(forms.ModelForm):

    id_empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        label="Empresa relacionada",
        to_field_name="id",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    pais = forms.MultipleChoiceField(
        choices=[],
        label="Países",
        widget=forms.SelectMultiple(attrs={"class": "form-select"}),
        required=False,
    )

    def get_countries_choices(self):
        return [(code, name) for code, name in countries]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["id_empresa"].label_from_instance = self.label_from_instance
        self.fields["pais"].choices = self.get_countries_choices()

    def label_from_instance(self, obj):
        return f"{obj.id} - {obj.nombre}"

    class Meta:
        model = AreaDeNegocio
        fields = ['nombre', 'pais', 'descripcion', 'id_empresa']

        