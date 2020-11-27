from django.shortcuts import render, redirect
from . import models
from .forms import TaskForm

# Create your views here.
def list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('/')


    else :
        tasks = models.Task.objects.all()
        form = TaskForm()
    return render(request, 'list.html', {'tasks' : tasks, 'form' : form})


def update(request, pk):
    task = models.Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid() :
            form.save()
            return redirect('/')
        
    return render(request, 'update.html', {'form' : form})


