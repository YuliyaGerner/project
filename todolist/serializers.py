from .models import Task
from rest_framework import serializers
from django.contrib.auth.models import User

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField()    

    class Meta:
        model = Task
        fields = ['user','title','complete','created','id']
