from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

def index(request):
    return HttpResponse('Hello world!')

def hello(request, name):
    return HttpResponse(f'Hello {name}')

def search(request):
    print(request.GET)
    # query = request.GET['q']        # Exception jos 'q' ei olemassa
    query = request.GET.get('q', 'oletusarvo')    # None jos 'q' ei olemassa
    if not query:
        return HttpResponse(f'Ok. Ei tullut mitään pyyntöä.')
    else:
        return HttpResponse(f'Ok. Yrität etsiä {query}')

def json_view(request):
    data = [{'key': 'value'}, {'name': 'Christian'}]
    return JsonResponse(data, safe=False)

def redirect(request):
    return HttpResponseRedirect('/hello/christian')