from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from aplicatie1.models import Location

# Create your views here.


class CreateIndexView(LoginRequiredMixin, CreateView):
    model = Location
    fields = '__all__'
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:home')


class HomeIndex(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    fields = '__all__'
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:home')