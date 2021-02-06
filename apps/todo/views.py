from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoForm


def todo_index(request):
    todos = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = Todo(
                description=form.cleaned_data['description'],
                state='pending',
            )
            todo.save()
            return redirect('/')
    context = {
        'todos': todos,
        'form': form,
    }
    return render(request, 'todo_index.html', context)


def remove(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    messages.info(request, 'ToDo removed')
    return redirect('/')


def edit(request, id):
    todo = Todo.objects.get(id=id)
    if (todo.state == 'pending'):
        todo.state = 'done'
    else:
        todo.state = 'pending'

    todo.save()
    messages.info(request, 'ToDo updated')
    return redirect('/')
