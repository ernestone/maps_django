from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def maps(request):
    """

    :param request:
    :return HttpResponse:

    """
    return render(request, 'maps.html', {"texto_enviado": "Esto es una prueba!!"})
