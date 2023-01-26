from django.shortcuts import render

def event(request):
    return render(request,"eventapp/event.html")

# Create your views here.
