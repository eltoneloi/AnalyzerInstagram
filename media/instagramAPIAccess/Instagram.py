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
    
    #Pega o texto associado a publicação
    def getListMediaText(self, json_string):
        list_media = json_string['data']
        list_text = []
        for i in list_media:
            try:
                list_text.append(i['caption']['text'])
            except:
                list_text.append('Sem texto')
        return list_text
    
    #Pega a quantidades de comentarios relacionadosa publicação
    def getListMediaCountComments(self, json_string):
        list_media = json_string['data']
        list_comments = []
        for i in list_media:
            list_comments.append(i['comments']['count'])
        return list_comments
    
    #Pega a qualidade de likes relacionados a publicação
    def getListMediaCountLikes(self, json_string):
        list_media = json_string['data']
        list_likes = []
        for i in list_media:
            list_likes.append(i['likes']['count'])
        return list_likes
    
    def getListMediaImg(self,json_string):
        list_media = json_string['data']
        list_img = []
        for i in list_media:
            list_img.append(i['images']['standard_resolution']['url'])
        return list_img
    
    
    #Usado para construir um dicionario com dados relevantes da media
    def agroupFieldsMedia(self, json_string):
        list_media = json_string['data']
        list_id = self.getListMediaId(json_string)
        list_img = self.getListMediaImg(json_string)
        list_likes = self.getListMediaCountLikes(json_string)
        list_comments = self.getListMediaCountComments(json_string)
        list_text = self.getListMediaText(json_string)
        result = []
        for i in range(len(list_media)):
            result.append([list_id[i], 
                           list_img[i], 
                           list_likes[i], 
                           list_comments[i], 
                           list_text[i]])
        
        return result
        
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
        