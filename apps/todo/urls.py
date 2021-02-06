from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_index, name='todo_index'),
    path('del/<int:id>/', views.remove, name='remove'),
    path('edit/<int:id>/', views.edit, name='edit'),
]
