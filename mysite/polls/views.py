from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You are at the poll index.")


def detail(request):
    print (request.body)
    return HttpResponse("hi there")
