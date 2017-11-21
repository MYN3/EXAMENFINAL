from django.db import models

from django.contrib import admin

# Create your models here.
class Materia(models.Model):
    nombre  =   models.CharField(max_length=30)
    profesor  =   models.CharField(max_length=30)
    def __str__(self):
        return self.nombre


class Grado(models.Model):
    nombre    = models.CharField(max_length=60)
    anio      = models.IntegerField()
    materias   = models.ManyToManyField(Materia, through='Imparte')
    def __str__(self):
        return self.nombre

class Imparte (models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

class ImparteInLine(admin.TabularInline):
    model = Imparte
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1

class MateriaAdmin(admin.ModelAdmin):
    inlines = (ImparteInLine,)

class GradoAdmin (admin.ModelAdmin):
    inlines = (ImparteInLine,)
