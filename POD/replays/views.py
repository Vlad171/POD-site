from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from replays.models import Replay
# Create your views here.

def replayslist(request):
    replay1=Replay.objects.order_by('-publishreplay')[0]
    replay2=Replay.objects.order_by('-publishreplay')[1]
    context={'replay1':replay1, 
             'replay2':replay2,
             }
    return render (request, 'replays/replays.html', context)


def replayview(request, slug):
	replayid=Replay.objects.get(slug=slug)
	return render(request,'replays/replaysdetail.html',{'replay':replayid})
