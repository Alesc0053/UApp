from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(reqeust):
    return HttpResponse("Index for washing machine")