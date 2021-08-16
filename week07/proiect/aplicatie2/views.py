from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from aplicatie2.models import Companies

# Create your views here.


class CreateCompaniesView(LoginRequiredMixin, CreateView):
    model = Companies
    fields = '__all__'
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('aplicatie2:listare')


class ListCompaniesView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'


class UpdateCompaniesView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = '__all__'
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('aplicatie2:listare')