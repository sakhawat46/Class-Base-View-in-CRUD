from django.db.models import indexes
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView
from first_app import models
# def index(request):
#     return HttpResponse("Hello")

class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'index.html'
