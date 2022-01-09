import json

from django.shortcuts import render
from django.http import HttpResponse


def job(request):
    if request.method == "GET":
        data = {
            "name": "sunanda",
            "Software": "fullstack"
        }
        print(request.GET)
        return HttpResponse(json.dumps(data))


def detail(request, question_id):
    if request.method == "POST":
        return HttpResponse("You're looking at question ."% question_id)


def results(request):
    if request.method == "GET":
        response = "You're looking at the results of question."
        return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("You're voting on question.")
