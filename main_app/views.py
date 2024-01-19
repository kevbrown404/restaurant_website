#...
from django.views.generic.base import TemplateView

from django.shortcuts import render
from django.urls import reverse
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

from .models import Review, Reservation
# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"
    
class ViewMenu(TemplateView):
    template_name = "view_menu.html"

class LeaveReview(CreateView):
    model = Review
    fields = ['name', 'email', 'review']
    template_name = "leave_review.html" 
    success_url = "/leave_review/"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.all()
        return context
    
    def form_valid(self, form):
        return super(LeaveReview, self).form_valid(form)



class ReservationCreate(CreateView):
    model = Reservation
    fields = ['name', 'email', 'date', 'time', 'party_size', 'special_requests']
    template_name = "reservation_create.html"
    success_url = "/reservation_create/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservations"] = Reservation.objects.all()
        return context

    def form_valid(self, form):
        return super(ReservationCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('reservation_detail', kwargs={'pk': self.object.pk})


class ReservationDetail(DetailView):
    model = Reservation
    template_name = "reservation_detail.html"

class ReservationUpdate(UpdateView):
    model = Reservation
    fields = ['name', 'email', 'date', 'time', 'party_size', 'special_requests']
    template_name = "reservation_update.html"
    success_url = "/reservations/"

    def get_success_url(self):
        return reverse('reservation_detail', kwargs={'pk': self.object.pk})

class ReservationDelete(DeleteView):
    model = Reservation
    template_name = "reservation_delete.html"
    success_url = "/reservation/new"

class ReservationSearch(TemplateView):
    template_name = "reservation_search.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["reservations"] = Reservation.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["reservations"] = Reservation.objects.filter()
            context["header"] = "Reservations"
        return context