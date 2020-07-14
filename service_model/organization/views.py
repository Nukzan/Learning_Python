from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def home(request):
    data = {'name' : 'hyein', 'Tel' : '0105555333', 'address' : 'nowhere'}
    return render(request, 'organization/home.html', context = data)
