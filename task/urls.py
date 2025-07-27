
from django.urls import path
from .views import home, toggle_task, delete_task

urlpatterns = [
    path('',home, name='home'),
    path('toggle/<int:task_id>/', toggle_task, name='toggle_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]