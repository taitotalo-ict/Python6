from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import ListView
from . import views
from .models import EsimerkkiMalli


app_name = "testi"
urlpatterns = [
    path('', views.index, name='homepage'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('search/', views.search),
    path('json/', views.json_view),
    path('redirect/', views.redirect),
    path('nimilista/', views.nimilista, name='nimilista'),
    # path('nimilista2/', views.Nimilista2.as_view()),
    path('nimilista3/', ListView.as_view(model=EsimerkkiMalli, template_name = 'testi/nimilista.html', context_object_name = 'names')),

    path('tervehdys/', views.TervehdysView.as_view()),
    path('contact/', views.contact_view),
    # path('products/', include('products.urls')) # projekti/products/urls.py
]



# products/urls.py
# urlpatterns = [
#     path('', views.index, name='products_homepage'), # products/
#     path('games/', views.index, name='products_games'), # products/games
# ]
