from django.http import JsonResponse
from django.shortcuts import render
from media.instagramAPIAccess.Instagram import Instagram
from media.WatsonNaturalLanguage.config import authenticate
from media.WatsonNaturalLanguage.WatsonAnalyze import WatsonAnalyze
from media.instagramAPIAccess.config import base_uri
# Create your views here.


def index(request):
    """Renderiza a pagina web principal da aplicção"""
    instagram = Instagram(base_uri)  #Instancia a classe do Instagram passando as urls para método construtor
    json_string = instagram.getSelfMedia() #Acessa o metodo da classe que pega todas as medias da api doinstagram
    media = instagram.agroupFieldsMedia(json_string) #Transforma a resposta json em uma lista de medias
    context = {'media':media} #Montagem do dicionario que será usado na redenrização do template
    return render(request,'media/media.html', context) #Renderiza a pagina html principal

#retorna o json com os dados do watson
def watsonResultJson(request):
    """Metodo igual ao rederWatsonResult,a unica difetença é o tipo de resposta. Neste caso,
    apenas retona um json"""
    if request.method == 'GET':
        media_id = request.GET['media_id']
        instagram = Instagram(base_uri)
        json_string = instagram.getComments(media_id = media_id)
        list_comments = instagram.getTextComments(json_string)
        merge_comments = instagram.mergeComments(list_comments)
        wa = WatsonAnalyze(authenticate)
        wa_response = wa.getResponse(merge_comments)
        
        return JsonResponse(wa_response)
    
def renderWatsonResult(request,media_id):
    if request.method == 'GET':  #Verifica se requisção foi feita pelo metodo get
        instagram = Instagram(base_uri) #Instancia a classe Instgram passando para construtor o dicionario de uri
        json_string = instagram.getComments(media_id = media_id) #Pega todos dos comentario de uma media
        list_comments = instagram.getTextComments(json_string) #Pega apenas o campo de comentario da restaposta json e trasnforma em uma lista
        merge_comments = instagram.mergeComments(list_comments)#Agrupa todas os comentarios da lista em um unico texto
        try:
            wa = WatsonAnalyze(authenticate) #Instacia a classe do Watson, passa o dicionairo de credenciais como parametro para metodo construtor
            wa_response = wa.getResponse(merge_comments) #Pega a resposta para do watson para o texto passado como parametro
        except:
            context={'Error':'True',
                     'Message':'Serviço indisponível no momento'}
            return render(request,'media/result.html', context)  #Retona um dicionario com erros para pagina caso tenha algum problema
        
        usage = wa.getDataUsage(wa_response)#Pega os dados de uso da resposta json
        lang = wa.getLanguage(wa_response) #Pega os dados de linguagem relacionados ao texto da resposta json
        keywords = wa.getKeywordsList(wa_response)#Pega as palavras chaves da resposta json do watson
        entities = wa.getEntityList(wa_response)#Pega todas as entidades identificadas pelo watson
        
        context = {'keywords':keywords, #Monta o dicionario
                   'entities': entities,
                   'usage': usage,
                   'language': lang}
        
    return  render(request,'media/result.html', context) #rederiza a pagina de resultados