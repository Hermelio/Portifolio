from django.shortcuts import render

# Create your views here.


def pagina_inicial(request):
    pagina = 'portifolio/base.html'

    return render(request, pagina)
