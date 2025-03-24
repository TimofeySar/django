from django.http import HttpResponse
from django.shortcuts import render
from pyexpat.errors import messages

from .models import *

def big_heading(x):
    return HttpResponse("<h1>big heading</h1>")

def small_heading(x):
    return HttpResponse("<h2>small heading</h2>")

l = ["hello", "world"]

def html_display(x):
    message = database.objects.all()
    return render(x, "index.html")

def ui_display(x):
    message = database.objects.all()
    return render(x, "UI.html",{"x": message})