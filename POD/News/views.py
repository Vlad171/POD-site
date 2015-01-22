from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from News.models import Event

# Create your views here.
def index(request):
    return render(request, 'News/index.html')

def clan(request):
	return render(request, 'News/clan.html')

def eventview(request):
	event_details=Event.objects.all()
	context={'Events':event_details}
	return render (request, 'News/Event.html', context)