from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task

# Import forms
from .forms import TaskForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task()
            task.task_title = form.cleaned_data['task_title']
            task.task_description = form.cleaned_data['task_description']
            task.save()
        

    form = TaskForm()

    all_taks = Task.objects.all()

    return render(request, 'checklist/index.html', {'form': form, 'all_tasks': all_taks})


def done(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.done = True
    task.save()

    return redirect('index')