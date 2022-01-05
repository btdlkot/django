from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Users

def index(request):
    users = Users.objects.all()
    return render(request, 'index.html', {'users': users})
