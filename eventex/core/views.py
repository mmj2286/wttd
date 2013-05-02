__author__ = 'mmj2286'

# coding: utf-8
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')