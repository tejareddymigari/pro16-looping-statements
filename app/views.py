from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'d':'mouni'}
    return render(request,'looping.html',d)