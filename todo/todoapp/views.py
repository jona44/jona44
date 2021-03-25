from django.shortcuts import render, redirect
from django.utils import timezone
from todoapp.models import Todo
from  django.http import HttpResponseRedirect

def home(request):
    todo_items =Todo.objects.all().order_by("-added_date")
    return render(request, 'todo/home.html', {'todo_items':todo_items})

def add_todo (request):
    current_date =timezone.now()
    content = request.POST["content"]
    created=Todo.objects.create(added_date=current_date, text=content)
    print(created)
    print(created.id)
    return HttpResponseRedirect ("/")

def delete_todo(request, todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect ("/")
