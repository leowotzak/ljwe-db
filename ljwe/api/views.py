from django.shortcuts import render
from django.http import HttpResponse
from .models import Symbol

def home(request):

    print(Symbol.objects.using('SecuritiesMaster').all())
    return HttpResponse('<h1>Blog Home</h1>')