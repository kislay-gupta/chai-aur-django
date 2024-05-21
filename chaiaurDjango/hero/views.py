from django.shortcuts import render

# Create your views here.
def all_hero(request):
    return render(request, 'hero/all_hero.html')