# category/views.py

from django.shortcuts import render, redirect
from .forms import CategoryForm
from django.contrib.auth.decorators import login_required

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('dashboard')
    else:
        form = CategoryForm()

    return render(request, 'category/add_category.html', {'form': form})
