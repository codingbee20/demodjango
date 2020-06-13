from django.shortcuts import render

# Create your views here.
def mydemosite(request):
    return  render(request, "mydemosite.html", {})