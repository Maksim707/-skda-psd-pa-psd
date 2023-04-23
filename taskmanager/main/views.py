from django.shortcuts import render, redirect
from .form import *
from .models import Magicnumber, New
from random import randint



def index(request):
     message = ""
     inputnum = Magicnumber.objects.get(id = 2).yrnum
     randynum = Magicnumber.objects.get(id = 2).compnum
     saver = Magicnumber.objects.get(id = 2)
     if request.method == "POST":
          form_a = MagicForm(request.POST, instance = Magicnumber.objects.get(id = 2))
          if form_a.is_valid():
               form_a.save()
               inputnum = Magicnumber.objects.get(id = 2).yrnum
          if inputnum == randynum:
               message = "Вроде да"
               randynum = randint(1, 20)
               saver.compnum = randynum
               saver.save()
          elif inputnum < randynum:
               message = 'маловато'
          else:
               message = 'что-то много'
     form = MagicForm
     context = {
          'form': form,
          "input": inputnum,
          "rand" : randynum,
          "message": message
     }
     return render(request, 'main/index.html', context)


def ilike(request):
     return render(request, 'main/ilike.html')


def news(request):
     allnew = New.objects.all()
     context = {
          'allnew': allnew
     }
     return render(request, 'main/news.html', context)

def createnews(request):
     error = ""
     if request.method == "POST":
          form = ForNews(request.POST)
          if form.is_valid():
               form.save()
               redirect('Magic')
     form = ForNews
     context = {
          'form': form,
          'error': error
     }
     return render(request, 'main/Newnews.html', context)