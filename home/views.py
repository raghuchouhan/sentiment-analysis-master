from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View, TemplateView

def choose_sentiment(request):
    return render(request, 'home/home.html')
