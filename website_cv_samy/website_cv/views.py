from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    return HttpResponse("""
        <h1> Welcome on my currilicum website !</h1>
        <p>The advanced scripting module is amazing !</p>
    """)

def view_portfolio(request, id_project):

    return HttpResponse(
        "You asked to see the project n° {0} !".format(id_project)
    )

