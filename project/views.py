from django.shortcuts import render


def homepage(req):
    return render(req, 'layout.html')