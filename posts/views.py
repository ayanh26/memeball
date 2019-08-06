from django.shortcuts import render
from .models import post

# Create your views here.

def home(request):
    allposts = post.objects
    return render(request, 'index.html', {'posts': allposts})
