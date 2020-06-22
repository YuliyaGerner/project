from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import *
from .forms import *


# Create your views here.


@login_required(login_url='signin')
def index(request):
    user = request.user

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Delete':
            task_id = request.POST['task_id']
            task = Task.objects.filter(pk=task_id).first()
            if task:
                task.delete()
        elif action == 'Complete':
            task_id = request.POST['task_id']
            task = Task.objects.get(id=task_id)
            task.complete = True
            task.save()
        elif action == 'Update':
            task_id = request.POST['task_id']
            task = Task.objects.get(pk=task_id)
            form = TaskForm(request.POST or None, instance=task)
            if form.is_valid():
               form.save()

            return render(request, 'todolist/update_task.html', {'form': form})

        # form = TaskForm(instance=task)

        # if request.method == 'POST':
        # form = TaskForm(request.POST, instance=task)
        # if form.is_valid():
        # form.save()
        # return redirect('/')
        # return render(request, 'todolist/update_task.html', {'form': form})
        elif action == 'Create Task':
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.user = user
                task.save()

        return HttpResponseRedirect(reverse_lazy('list'))
    elif request.method == 'GET':
        form = TaskForm()
        tasks = Task.objects.filter(user=user)
        context = {
            'tasks': tasks,
            'form': form,
            'user': user
        }
        return render(request, 'todolist/list.html', context)


# @login_required
# def tasks_for_user(request):
# 	tasks = Task.objects.filter(user=request.user)
# 	return render(request, 'todolist/list.html', {'tasks' : tasks})
#
#
# def updateTask(request, pk):
# 	task = Task.objects.get(id=pk)
#
# 	form = TaskForm(instance=task)
#
# 	if request.method == 'POST':
# 		form = TaskForm(request.POST, instance=task)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')
#
# 	context = {'form': form}
#
# 	return render(request, 'todolist/update_task.html', context)
#
#
# def deleteTask(request, pk):
# 	item = Task.objects.get(id=pk)
#
# 	if request.method == 'POST':
# 		if item == 'delete':
# 			item.delete()
# 			return redirect('/')
#
# 	context = {'item': item}
# 	return render(request, 'todolist/list.html', context)


def aboutPage(request):
    return render(request, 'todolist/about.html')
