from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
    return render(request, 'News/index.html')

def clan(request):
	return render(request, 'News/clan.html')