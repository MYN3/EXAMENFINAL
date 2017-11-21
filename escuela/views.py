from django.shortcuts import render

#librería para manejar el envío de mensajes

from django.contrib import messages
from .forms import GradoForm
from escuela.models import Grado, Materia, Imparte

def grado_nuevo(request):

    if request.method == "POST":

        formulario = GradoForm(request.POST)

        if formulario.is_valid():

            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])

            for materia_id in request.POST.getlist('materias'):

                imparte = Imparte(materia_id=materia_id, grado_id = grado.id)

                imparte.save()

            messages.add_message(request, messages.SUCCESS, 'Grado Guardado Exitosamente')

    else:

        formulario = GradoForm()

    return render(request, 'escuela/grado_editar.html', {'formulario': formulario})
