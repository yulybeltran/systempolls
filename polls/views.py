from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(reques):
  return HttpResponse("Hello, world. poll app index")


