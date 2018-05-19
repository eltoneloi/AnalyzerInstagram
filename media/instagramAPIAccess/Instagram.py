# -*- coding: utf-8 -*-
import requests
import json

class Instagram:
    def __init__(self,baseURI):
        self.baseURI = baseURI
    #Pega a resposta json de qualquer url passada como parametro
    def getJsonFromURI(self,uri):
        response = requests.request("GET",uri)
        content = response.content
        json_string = json.loads(content)
        return json_string
    #pega os dados de usuario
    def getSelfUser(self):
        json_string = self.getJsonFromURI(self.baseURI['get_user'])
        return json_string
    
    #pega o json com todas a medias recentes
    def getSelfMedia(self):
        json_string = self.getJsonFromURI(self.baseURI['get_media'])
        return json_string
        
    #retorna os id de todas as medias do json
    def getListMediaId(self,json_string):
        list_media = json_string['data']
        list_id = []
        for i in list_media:
            list_id.append(i['id'])
        return list_id
    
    #pega o json com todos os comentarios de uma media especifica
    def getComments(self, media_id):
        string = self.baseURI['get_comments']
        string = string.replace("{media-id}",str(media_id))
        json_string = self.getJsonFromURI(string)
        return json_string
    
    #Transforma os comentarios do json em uma lista de apenas com os textos
    def getTextComments(self,comments_json):
        list_comments = []
        for i in comments_json['data']:
            list_comments.append(i['text'])
        return list_comments
        