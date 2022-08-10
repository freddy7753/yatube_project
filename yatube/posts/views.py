from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('домашняя страница сайта для блогов')

def group_posts(request, slug):
    return HttpResponse('страница для блога')