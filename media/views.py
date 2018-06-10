from django.http import JsonResponse
from django.shortcuts import render
from media.instagramAPIAccess.Instagram import Instagram
from media.WatsonNaturalLanguage.config import authenticate
from media.WatsonNaturalLanguage.WatsonAnalyze import WatsonAnalyze
from media.instagramAPIAccess.config import base_uri
# Create your views here.


def index(request):
    instagram = Instagram(base_uri)
    json_string = instagram.getSelfMedia()
    media = instagram.agroupFieldsMedia(json_string)
    context = {'media':media}
    return render(request,'media/media.html', context)

#retorna o json com os dados do watson
def watsonResultJson(request):
    if request.method == 'GET':
        media_id = request.GET['media_id']
        instagram = Instagram(base_uri)
        json_string = instagram.getComments(media_id = media_id)
        list_comments = instagram.getTextComments(json_string)
        merge_comments = instagram.mergeComments(list_comments)
        wa = WatsonAnalyze(authenticate)
        wa_response = wa.getResponse(merge_comments)
        
        return JsonResponse(wa_response)
    
def renderWatsonResult(request):
    if request.method == 'GET':
        media_id = request.GET['media_id']
        instagram = Instagram(base_uri)
        json_string = instagram.getComments(media_id = media_id)
        list_comments = instagram.getTextComments(json_string)
        merge_comments = instagram.mergeComments(list_comments)
        wa = WatsonAnalyze(authenticate)
        wa_response = wa.getResponse(merge_comments)
        keywords = wa.getKeywordsList(wa_response)
        entities = wa.getEntityList(wa_response)
        usage = wa.getDataUsage(wa_response)
        lang = wa.getLanguage(wa_response)
        
        context = {'keywords':keywords, 
                   'entities': entities,
                   'usage': usage,
                   'language': lang}
        
    return  render(request,'media/result.html', context)