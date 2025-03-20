from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = "testi"
urlpatterns = [
    path('', views.index, name='homepage'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('search/', views.search),
    path('json/', views.json_view),
    path('redirect/', views.redirect)
    # path('products/', include('products.urls')) # projekti/products/urls.py
]



# products/urls.py
# urlpatterns = [
#     path('', views.index, name='products_homepage'), # products/
#     path('games/', views.index, name='products_games'), # products/games
# ]
