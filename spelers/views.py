from django.shortcuts import render
from .models import Voetbalspelers


def post_list(request):
    spelers = Voetbalspelers.objects.all()
    return render(request, 'spelers/post_list.html', {'spelers': spelers})