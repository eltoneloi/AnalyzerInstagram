# -*- coding: utf-8 -*-

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

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
        json_string = json.loads(response)
            
        return json_string
    
    def getDataUsage(self, watson_response):
        return (watson_response['usage']['text_units'],
                watson_response['usage']['text_characters'],
                watson_response['usage']['features'])
    
    def getLanguage(self, watson_response):
        return watson_response['language']
    
    
    def getKeywords(self, watson_reponse):
        
            