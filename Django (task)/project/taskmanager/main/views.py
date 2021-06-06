from .forms import TaskForm
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .models import Task



def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html', {})


def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма некорректна'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): # проверка пароля на требования по символам и т.д
            form.save()
            return redirect('index') # перевод на другую страницу
        else:
            return render(request, 'registration/register.html', {'form': form})
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
