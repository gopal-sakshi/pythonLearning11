from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Django views ===> Python functions that take http requests & returns http response

# members14 == name of the view
def members14(request):

    # render html via templateFolder
    template = loader.get_template('nadal11.html')
    return HttpResponse(template.render())

    # # return simple http response
    # return HttpResponse("Hello world!")