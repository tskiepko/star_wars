from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class PhotoList(TemplateView):
    template_name = "PhotoList.html"