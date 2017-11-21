from django import forms

from .models import Grado, Materia


class GradoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Grado
        fields = ('nombre', 'anio', 'materias')

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.

#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.


        def __init__ (self, *args, **kwargs):
            super(GradoForm, self).__init__(*args, **kwargs)
            self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["materias"].help_text = "Ingrese las Materias que se impartiran en el Grado"
            self.fields["materias"].queryset = Materia.objects.all()
