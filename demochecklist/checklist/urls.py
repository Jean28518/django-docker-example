from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('done/<int:task_id>/', views.done, name='done'),
]