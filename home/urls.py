from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.choose_sentiment, name="choose_sentiment"),
    
]