from django.shortcuts import render,HttpResponse,redirect
import os

# Create your views here.
def home(request):
    return redirect("listofmovies")

def listofmovies(request):

    allvids=[]
    count=0
    for root, dirs, files in os.walk(".", topdown=False):
        count+=1
        for name in files:
            if name.endswith(".mp4") or name.endswith(".mkv"):
                allvids.append(name)

    context={
        "allvids":allvids
    }
    return render(request,"videoplayer/list.html",context)

def player(request,name):

    context={
        "name":name
    }
    return render(request,"videoplayer/videoplayer.html",context)
