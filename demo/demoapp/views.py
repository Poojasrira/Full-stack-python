from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

# Function-based view
def hello_world(request):
    return HttpResponse("hello world")


# Class-based view
class HelloIndia(View):
    def get(self, request):
        return HttpResponse("hello India")


# Function-based view
def home(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    else:
        form = ReservationForm()

    return render(request, "index.html", {"form": form})