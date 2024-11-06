from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'), # incluiremos la lista de tareas para que nuestro enrutador de URL no pueda usar una clase dentro de ella
    # se usa un metodo que esta vista tiene as_view() y activara una función dentro de esa vista dependiendo del tipo de metodo,
    # de modo que si es POST o REQUEST, sabrá qué hacer
    # el view de forma predeterminada busca una clave principal, por lo que es un valor pk, por lo que en este caso se configura en pk
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]