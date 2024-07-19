from django.http import HttpResponse

''' aws db admin - admin123'''


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")