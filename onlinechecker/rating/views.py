from django.shortcuts import render
from datetime import datetime

from .models import WaveRating
# Create your views here.
from django.http import HttpResponse


def index(request):
    if(request.method == 'POST'):
        data = request.POST.copy()
        rating = int(data['rating'])

        entry = WaveRating(
            rating = rating,
            ip = '0.0.0.0',
            date = datetime.now()

        )
        entry.save()

        return render(request, 'rating/success.html')

    return render(request, 'rating/index.html',{})