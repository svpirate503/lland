from django.shortcuts import render
from .models import Post 
def index(request):

    p = Post.objects.all()
    return render(request,'index.html',{'postt':p})


def services(request):
    postk = Post.objects.all()
    return render(request,'services.html',{'post':postk})