from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, '../templates/wordcount/home.html')


def count(request):
    fulltext = request.GET['fulltext']
    count = len(fulltext.split())

    return render(request, '../templates/wordcount/count.html', {
        'fulltext': fulltext,
        'count': count
    })