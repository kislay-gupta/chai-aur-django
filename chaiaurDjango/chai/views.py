from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404
def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html',{'chais':chais})

def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request,'chai/chai_details.html', {'chai':chai})