from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    print(todos)
    context= {
        "todo_list": todos
    }
    return render(request, "todo/todo_list.html", context)

    #CRUD - Create, Retrieve, Update, Delete, ;;; List

def todo_detail(request, id):
    todo = Todo.objects.get(id = id)
    context = {
        "todo": todo
    }
    return render(request, "todo/todo_detail.html", context)

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        # create a todo objet
        print(form.cleaned_data)
        pass
    context = {"form": form}
    return render(request, "todo/todo_create.html", context)
        