from django.conf.urls import url
from django.urls import path, include
from . import views
from .views import aboutPage
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)


urlpatterns = [
    path('', views.index, name="list"),
    path('update_task/<int:task_id>/', views.index, name="Update"),
    #path('delete/<int:task_id>/', views.deleteTask, name="delete"),
    #path('about/', views.aboutPage, name="about"),
    path('api/', include(router.urls)),
]
