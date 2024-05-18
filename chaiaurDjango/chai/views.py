from django.shortcuts import render

def all_chai(request):
    return render(request, 'all_chai.html')