from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import SearchForm
from django.http import HttpResponse
from .models import Tata
from django.db.models import Q
# Create your views here.

class HomePageView(ListView):
    model = Tata
    template_name = 'base.html'
    
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            object_list = self.model.objects.filter(name__icontains=q)

import urllib.request
import json

class ResultView(ListView):
    model = Tata
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        key='9e0ada34da2b1b28611fee7bca2c6d21'
        apilink = 'https://api.openweathermap.org/data/2.5/weather?q='+ query +'&appid='+ key
        apilink = apilink.replace(" ","%20")
        getapi = urllib.request.urlopen(apilink).read()
        dataset = json.loads(getapi)
        data = {
            "cod" : dataset['cod']
        }
        data = {
            "city" : dataset['name'],
            "temp" : dataset['main']['temp'],
            "humidity" : dataset['main']['humidity'],
        }
        ct = str(data['city'])
        humi = int(data['humidity'])
        temp = int(data['temp']) - 273
        self.temp = temp
        self.humidity = humi
        self.city = ct
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        object_list = Tata.objects.filter(
            Q(maxTemp__gte=self.temp),Q(minTemp__lte=self.temp))
        return object_list
    
    def get_context_data(self,*args, **kwargs):
        context = super(ResultView, self).get_context_data(*args,**kwargs)
        context['temp'] = self.temp
        context['humidity'] = self.humidity
        context['city'] = self.city
        return context

#Error
from django.shortcuts import render

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)