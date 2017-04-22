from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):

    return HttpResponse("Hello")


# return render(request, 'faq/faq.html', context)
