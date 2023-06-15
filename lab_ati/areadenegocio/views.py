from django.shortcuts import redirect, render
from django.urls import reverse
from lab_ati.areadenegocio.forms import AreaDeNegocioForm

from lab_ati.areadenegocio.models import AreaDeNegocio

def areasdenegocio(request, business_id):
    context = {}
    context['business_id'] = business_id
    areasdenegocio = AreaDeNegocio.objects.all()  # Consulta todas las áreas de negocio
    context['areasdenegocio'] = areasdenegocio

    return render(request, 'pages/areanegocio/index.html', context)

def ver_areadenegocio(request, id, business_id):
    context = {}
    context['business_id'] = business_id
    areadenegocio = AreaDeNegocio.objects.get(id = id)
    context['form'] = AreaDeNegocioForm(request.POST or None, instance=areadenegocio)
    context["list_link"] = reverse("areasdenegocio", kwargs={"business_id": business_id} )
    context["nombre_empresa"] = areadenegocio.id_empresa

    return render(request, 'pages/areanegocio/verAreaNegocio.html', context)


def crear_areadenegocio(request, business_id):
    context = {}
    context['business_id'] = business_id
    
    if request.method == 'POST':
        form = AreaDeNegocioForm(request.POST)
        
        if form.errors:
            print(form.errors)

        if form.is_valid():
            area_de_negocio = form.save()  # Guardar el área de negocio en la base de datos
            # Hacer cualquier otra lógica adicional si es necesario
            print('GUARDEEEE BIIIIHH')

            return redirect('areasdenegocio', business_id = business_id)
    else:
        form = AreaDeNegocioForm()

    context['form'] = form
    context["list_link"] = reverse("areasdenegocio", kwargs={"business_id": business_id} )

    return render(request, 'pages/areanegocio/create.html', context)

def eliminar_areadenegocio(request, id, business_id):
    areadenegocio = AreaDeNegocio.objects.get(id = id)
    areadenegocio.delete()
    context = {}
    context["list_link"] = reverse("areasdenegocio", kwargs={"business_id": business_id} )
    context['business_id'] = business_id

    return redirect('areasdenegocio', business_id = business_id)

def editar_areadenegocio(request, id, business_id):
    context = {}
    context['business_id'] = business_id
    areadenegocio = AreaDeNegocio.objects.get(id = id)
    form = AreaDeNegocioForm(request.POST or None, instance=areadenegocio)
    if form.is_valid() and request.POST:
        savedForm = form.save()
        return redirect('areasdenegocio', business_id = business_id)
    
    context['form'] = form
    context["list_link"] = reverse("areasdenegocio", kwargs={"business_id": business_id} )

    return render(request, 'pages/areanegocio/editar.html', context)