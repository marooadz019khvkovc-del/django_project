from django.shortcuts import render
from .models import Trainee

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'app1/trainee_list.html', {'trainees': trainees})