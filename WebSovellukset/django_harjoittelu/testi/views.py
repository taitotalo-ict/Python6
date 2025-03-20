from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import EsimerkkiMalli
from .forms import ContactForm


def index(request):
    context = {'title': 'Homepage'}
    return render(request, 'testi/index.html', context=context)
    # return HttpResponse('Hello world!')

def hello(request, name):
    context = {
        'title': 'Hello',
        'name': name,
    }
    return render(request, 'testi/index.html', context=context)
    # return HttpResponse(f'Hello {name}')

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
    return HttpResponseRedirect(reverse('tests:hello', args=['christian']))
    # return HttpResponseRedirect(reverse('hello', kwargs={'name':'christian'}))


def nimilista(request):
    lista = EsimerkkiMalli.objects.all()
    return render(request, 'testi/nimilista.html', context={'names': lista})

class TervehdysView(View):
    def get(self, request):
        return HttpResponse('Moikka!')

# class Nimilista2(ListView):
#     model = EsimerkkiMalli
#     template_name = 'testi/nimilista.html'
#     context_object_name = 'names'

def contact_view(request):
    if request.method == 'GET':
        form = ContactForm
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            context = {}
            context['name'] = form.cleaned_data['name']
            context['email'] = form.cleaned_data['email']
            context['message'] = form.cleaned_data['message']
            return render(request, 'testi/thanks.html', context={'data': context})

    return render(request, 'testi/contact.html', {'form': form})


# Koko sivuston etusivu
def etusivu(request):
    return HttpResponse('Etusivu')

