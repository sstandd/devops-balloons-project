from django.shortcuts import render, redirect
from .forms import FlightsForm
from .models import Flight
from django.db.models import Q


# Create your views here.

def index(request):
    return render(request, "index.html")


def flights(request):
    if request.method == "POST":
        form_data = FlightsForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            flight = form_data.save(commit=False)
            flight.user = request.user
            flight.image = form_data.cleaned_data['image']
            flight.save()
            return redirect('flights')
    else:
        form = FlightsForm()
    flights = Flight.objects.filter(
        Q(airport_from__iexact="Skopje") | Q(airport_from__iexact="Скопје")).all()
    context = {'flights': flights, 'form': form}
    return render(request, 'flights.html', context)
