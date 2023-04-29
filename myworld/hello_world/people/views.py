#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import People

def people(request):
    mypeople = People.objects.all().values()
    template = loader.get_template('all_people.html')
    context = {
        'mypeople': mypeople,
    }
    return HttpResponse(template.render(context, request))
def details(request, id):
    myperson = People.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myperson': myperson,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template  = loader.get_template('template.html')
    context  = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))
