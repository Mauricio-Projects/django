from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello Word<h1>')

def about(request):
    return HttpResponse('<h2>about<h2>')
