# -*- coding: utf-8 -*-

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

class Keyword:
    def __init__(self, text, 
                 sentiment_score,
                 relevance,
                 emotion_sadness,
                 emotion_joy,
                 emotion_fear,
                 emotion_disgust,
                 emotion_anger):
        self.text = text
        self.sentiment_score = sentiment_score
        self.relevance = relevance
        self.emotion_sadness = emotion_sadness
        self.emotion_joy = emotion_joy
        self.emotion_fear = emotion_fear
        self.emotion_disgust = emotion_disgust
        self.emotion_anger = emotion_anger
        
        
        
        
        
        
class Entity(Keyword):
    def __init__(self, type_entity ,text, 
                 sentiment_score,
                 relevance,
                 emotion_sadness,
                 emotion_joy,
                 emotion_fear,
                 emotion_disgust,
                 emotion_anger):
        super().__init__(text, 
                 sentiment_score,
                 relevance,
                 emotion_sadness,
                 emotion_joy,
                 emotion_fear,
                 emotion_disgust,
                 emotion_anger)
        self.type_entity = type_entity
        
        
        
        
        
        
class WatsonAnalyze:
    
    def __init__(self, authenticate):
        self.natural_language_understanding = NaturalLanguageUnderstandingV1(
                username=authenticate['username'],
                password=authenticate['password'],
                version=authenticate['version'])
    
    def getResponse(self, text):
        response = self.natural_language_understanding.analyze(
                text= text,
                features=Features(entities=EntitiesOptions(
                        emotion=True,
                        sentiment=True,
                        limit=2),
                keywords=KeywordsOptions(
                        emotion=True,
                        sentiment=True,
                        limit=2)))
        json_string = json.loads(json.dumps(response))
            
        return json_string
    
    def getDataUsage(self, watson_response):
        return (watson_response['usage']['text_units'],
                watson_response['usage']['text_characters'],
                watson_response['usage']['features'])
    
    def getLanguage(self, watson_response):
        return watson_response['language']
    
    
    def getKeywordsList(self, watson_response):
        keyword_list = []
        if len(watson_response['keywords']) > 2:
            for key in watson_response['keywords']:
                keyword_list.append(Keyword(key['text'],
                                            key['sentiment']['score'],
                                            key['relevance'],
                                            key['emotion']['sadness'],
                                            key['emotion']['joy'],
                                            key['emotion']['fear'],
                                            key['emotion']['disgust'],
                                            key['emotion']['anger']
                                            ))
        return keyword_list
        
    def getEntityList(self, watson_response):
        entity_list = []
        if len(watson_response['entities']) >2:
            for key in watson_response['entities']:
                entity_list.append(Entity(key['type'],
                                          key['text'],
                                          key['sentiment']['score'],
                                          key['relevance'],
                                          key['emotion']['sadness'],
                                          key['emotion']['joy'],
                                          key['emotion']['fear'],
                                          key['emotion']['disgust'],
                                          key['emotion']['anger']
                                          ))
        return entity_list
            