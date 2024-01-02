from django.shortcuts import render
from django.http import HttpResponse
from lockdown.decorators import lockdown


# Create your views here.

def Home(request):
    return render(request,'app/index.html')
    
    