from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, blog!")
# Create your views here.
