from django.conf.urls import url
from django.urls import path, include
from . import views
from .views import aboutPage


urlpatterns = [
    path('', views.index, name="list"),
    #path('update_task/<int:task_id>/', views.index, name="Update"),
    #path('delete/<int:task_id>/', views.deleteTask, name="delete"),
    path('about/', views.aboutPage, name="about"),    
]
