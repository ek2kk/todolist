from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.generic import UpdateView, DeleteView
import datetime


# Create your views here.


def index(request):
    todos = Todo.objects.order_by('date_to_complete')
    tag = 0
    for todo in todos:
        if todo.is_done is False:
            tag = 1
            break
    return render(request, 'main/index.html', {'title': 'Список дел', 'todos': todos, 'tag': tag})


def archive(request):
    todos = Todo.objects.order_by('date_to_complete')
    tag = 0
    for todo in todos:
        if todo.is_done is False:
            tag = 1
            break
    return render(request, 'main/archive.html', {'title': 'Архив', 'todos': todos, 'tag': tag})


def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
        else:
            error = 'Форма была заполнена неверно'
    form = TodoForm()
    data = {
        'form': form,
        'error': error,
        'title': 'Создать задачу'
    }
    return render(request, 'main/create.html', data)


class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'main/create.html'
    form_class = TodoForm


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = '/'
    template_name = 'main/delete.html'


def done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect('/')