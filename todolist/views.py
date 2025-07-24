from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todolist/dashboard.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'todolist/add_task.html', {'form': form})

@login_required
def edit_task(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todolist/edit_task.html', {'form': form})

@login_required
def delete_task(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    task.delete()
    return redirect('dashboard')
