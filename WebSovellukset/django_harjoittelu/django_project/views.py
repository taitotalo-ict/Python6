from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world!')

def hello(request, name):
    return HttpResponse(f'Hello {name}')