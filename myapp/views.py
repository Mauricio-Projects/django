from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render

# Create your views here.


def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = 'fazt'
    return render(request, 'about.html', {
        'username': username
    })


def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def tasks(request):
    # task = Task.objects.get(title=tile)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })