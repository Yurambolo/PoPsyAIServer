from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from apis import models
import jsonpickle
import json
from django.views.decorators.csrf import csrf_exempt
from apis.AI.Recomedation import  Rcomendaror
from apis.AI.TextAI import TextAI
import numpy as np

recomendator = Rcomendaror()
textAI = TextAI()

@csrf_exempt
def extractEnotion(request):
    Text = jsonpickle.decode(request.POST.get("Text"))
    return JsonResponse(jsonpickle.encode(textAI.predictEmotion(Text),unpicklable=True),safe = False)

@csrf_exempt
def NearestUserEmotion(request):
    currentUserEmotions = jsonpickle.decode(request.POST.get("currentUserEmotions"))
    otherUserEmotions = jsonpickle.decode(request.POST.get("otherUserEmotions"))
    nearestUserEmotion = recomendator.get_nearest(currentUserEmotions, otherUserEmotions)
    nearestUserEmotion = jsonpickle.encode(nearestUserEmotion,unpicklable=True)
    return JsonResponse(nearestUserEmotion,safe = False)

@csrf_exempt
def GenerateRecomendations(request):
    playlists = jsonpickle.decode(request.POST.get("playlists"))
    videolists = jsonpickle.decode(request.POST.get("videolists"))
    articles = jsonpickle.decode(request.POST.get("articles"))
    playlistsView = jsonpickle.decode(request.POST.get("playlistsView"))
    videolistsView = jsonpickle.decode(request.POST.get("videolistsView"))
    articlesView = jsonpickle.decode(request.POST.get("articlesView"))
    audioRecomndations, videoRecomendations, articleRecomendations = recomendator.generate_recomendations(playlists, videolists, articles, playlistsView, videolistsView, articlesView)
    map = {"audioRecomndations": jsonpickle.encode(audioRecomndations, unpicklable=True), "videoRecomendations": jsonpickle.encode(videoRecomendations, unpicklable=True), "articleRecomendations": jsonpickle.encode(articleRecomendations, unpicklable=True)}
    return JsonResponse(map, safe = False)