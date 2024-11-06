from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    # necesitamos crear una relación uno a muchos, podemos tener un usuario y ese usuario puede tener muchos elementos
    # se puede configurar con valores de clave foránea
    # on_delete significa que hacemos con una tarea si el usuario se elimina, por lo que si el usuario se elimina, sus tareas también
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # se usará para el nombre del título de la tarea
    title = models.CharField(max_length=100)
    # se usa TextField porque si esto fuera un formulario, nos daría un cuadro para escribir un mensaje más extenso
    description = models.TextField(null=True, blank=True)
    # se usará un booleano para saber si esta terminada la tarea o no
    complete = models.BooleanField(default=False)
    # se usará para establecer la fecha en que se creó la tarea
    created = models.DateTimeField(auto_now_add=True)

    # para cambiar o cerrar esto, se configura el valor de cadena, pasando el self que será una representación de cadena del modelo
    # y su nombre
    def __str__(self):
        return self.title
    # se ordenarán los elementos por el estado completo, por lo que cualquier elemento completo debe enviarse al final de la lista
    # porque ya está listo y no necesitamos centrarnos en ellos
    class Meta:
        ordering = ['complete']