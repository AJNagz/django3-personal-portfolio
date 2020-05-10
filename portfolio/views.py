from django.shortcuts import render
# this import will add all the models (database)
from .models import Project


def home(request):
    # projects variable will get all the database object
    projects = Project.objects.all()
    # here we created a dictionary to access the objects
    return render(request, 'portfolio/home.html', {'projects':projects})


