from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from News.models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'News/index.html')

def clan(request):
	return render(request, 'News/clan.html')

def eventview(request):
    members = requests.get('https://api.worldoftanks.ru/wot/clan/info/?application_id=demo&clan_id=27603')
    count=members.json()
    memcounts=count["data"]["27603"]['members_count']
    rankclan=requests.get('https://api.worldoftanks.ru/wot/clanratings/clans/?application_id=demo&type=all&clan_id=27603')
    rank=rankclan.json()
    ourrank=rank["data"]["27603"]["efficiency"]["rank"]
    deltarank=rank["data"]["27603"]["efficiency"]["rank_delta"]
    globalrank=rank["data"]["27603"]["elo_rating_gm"]["rank"]
    deltaglobal=rank["data"]["27603"]["elo_rating_gm"]["rank_delta"]
    ##news1=Event.objects.order_by('-publish')[0]
    ##news2=Event.objects.order_by('-publish')[1]
    ##context={'news1':news1, 
             ##'news2':news2,
             ##'memcounts':memcounts,
             ##'ourrank':ourrank,'delta':deltarank, 
             ##'globalrank':globalrank, 
             ##'deltaglobal':deltaglobal}###

    bynews = Event.objects.all()
    paginator = Paginator(bynews, 2) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
         news = paginator.page(paginator.num_pages)

    return render(request,'News/news.html', {'news': news,
        'memcounts':memcounts,
        'ourrank':ourrank,
        'delta':deltarank,
        'globalrank':globalrank,
        'deltaglobal':deltaglobal})
    ##return render (request, 'News/news.html', context)

def eventdetail(request, slug):
	detailnews=Event.objects.get(slug=slug)
	return render(request,'News/Event_detail.html',{'detailnews':detailnews})



	 