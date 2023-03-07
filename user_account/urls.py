from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.create_task, name='create_task'),
    path('account/', views.account, name='account'),
]