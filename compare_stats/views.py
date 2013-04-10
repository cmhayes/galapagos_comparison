# Create your views here.
from compare_stats.models import State, Galapagos
from django.shortcuts import render, get_object_or_404, redirect, render_to_response

def home(request):
    states = State.objects.all()
    galapagos = Galapagos.objects.all()
    context = {
        'states': states,
        'galapagos': galapagos,
    }
    
    return render(request, "compare_stats/home.html", context)

def location(request, pk):
    specificState = get_object_or_404(State, id=pk)
    specificGalapagos = get_object_or_404(Galapagos, id=pk)
    context = {
        'specificState': specificState,
        'specificGalapagos': specificGalapagos,
    }