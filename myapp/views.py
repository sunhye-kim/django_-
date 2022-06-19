from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):

    # http 로 응답을 하겠다
    return HttpResponse('Welcome!')