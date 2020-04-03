from django.shortcuts import render
from .models import Projectss

def home(request):
    blog = Projectss.objects.all()
    context = {
        'blog': blog
    }
    return render(request, 'base/home.html', context)
