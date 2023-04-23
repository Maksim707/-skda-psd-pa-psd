from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='Magic'),
     path('ilike', views.ilike, name='Feature'),
     path('news', views.news, name='News'),
     path('Newnews', views.createnews, name='Newnews')
]
