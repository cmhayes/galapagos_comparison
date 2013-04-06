# Create your views here.
from compare_stats.models import State
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
#from chartit import PivotDataPool, PivotChart

def home(request):
    
    return render(request, "compare_stats/home.html")