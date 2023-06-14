from django.shortcuts import redirect, render

def areasdenegocio(request, business_id):
    context = {}
    context['business_id'] = business_id


    return render(request, 'pages/areanegocio/index.html', context)

def ver_areadenegocio(request, id, business_id):
    context = {}
    context['business_id'] = business_id

    return render(request, 'pages/areanegocio/verAreaNegocio.html', context)


def crear_areadenegocio(request, business_id):
    context = {}
    context['business_id'] = business_id

    return render(request, 'pages/areanegocio/create.html', context)


def eliminar_areadenegocio(request, business_id):
    context = {}
    context['business_id'] = business_id

    return redirect('areasdenegocio', business_id = business_id)


def editar_areadenegocio(request, business_id):
    context = {}
    context['business_id'] = business_id

    return render(request, 'pages/areanegocio/editar.html', context)

