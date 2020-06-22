from django import forms
from django.forms import ModelForm

from .models import Task



class TaskForm(forms.ModelForm):
	title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
	class Meta:
		model = Task
		#exclude = ['user', 'complete', 'created']
		fields = '__all__'