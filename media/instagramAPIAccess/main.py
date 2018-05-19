# -*- coding: utf-8 -*-

from config import app_authenticate, base_uri
from Instagram import Instagram

instagram = Instagram(base_uri)
#instagram.getSelfUser()
list_media=instagram.getListMediaId(instagram.getSelfMedia())
comments_json = instagram.getComments(list_media[0])
instagram.getTextComments(comments_json)