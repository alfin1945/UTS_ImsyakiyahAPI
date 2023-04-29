from django.shortcuts import render
 
def index(request):
    return render (request, 'index.html'),

def coba(request):
    return render (request, 'coba.html')