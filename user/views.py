from django.shortcuts import render
from array import array
from django.http import HttpResponse
import json

def dashboard(request):
    return render(request, 'user/dashboard.html')
