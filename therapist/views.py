from django.shortcuts import render
from therapist.models import Psychotherapists
# Create your views here.


def show therapist():
    return render(request, 'index.html')
