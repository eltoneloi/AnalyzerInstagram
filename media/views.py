from django.shortcuts import render
from media.instagramAPIAccess.Instagram import Instagram
from media.instagramAPIAccess.config import base_uri
# Create your views here.

def index(request):
    instagram = Instagram(base_uri)
    json_string = instagram.getSelfMedia()
    media = instagram.agroupFieldsMedia(json_string)
    context = {'media':media}
    return render(request,'media/media.html', context)