from django.shortcuts import render

# Create your views here.

def mathadd(request):
    context = {}
    return render(request,'mathapp/mathadd.html',context)

def matharea(request):
    context = {}
    return render(request,'mathapp/matharea.html',context)

def bootstrap(request):
    context = {}
    return render(request,'mathapp/bootstrap.html',context)