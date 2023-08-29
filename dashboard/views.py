from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello!")


def baseball(request):
    return HttpResponse("Baseball page")


def basketball(request):
    return HttpResponse("basketball page")


def football(request):
    return HttpResponse("football page")
