from django.shortcuts import render
from django.shortcuts import redirect
from .models import UrlModel
# Create your views here.

def urlRedirect(request,key):
    link=UrlModel.objects.get(key_url=key).value_url
    return redirect("/hestiatkmce.live/{}".format(link))

def event_view(request):
    return render(request,"events.html")

def hackathon_view(request):
    return render(request,"hackathon.html")

def main_view(request):
    return render(request,"home.html")

def proshow_view(request):
    return render(request,"proshow.html")




