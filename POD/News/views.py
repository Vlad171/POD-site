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
	event_details1=Event.objects.order_by('-publish')[:1]
	event_details2=Event.objects.order_by('-publish')[1:2]
	
	context={'Events1':event_details1, 'Events2':event_details2}
	return render (request, 'News/index.html', context)