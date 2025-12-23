from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
# request -> response

# What we are doing here is creating a function for every html page with the aim to return the html interface
def homepage(request):
  return render(request, 'index.html')
