from django.shortcuts import render

# Create your views here.
from serviceapp.models import Service
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ServiceList(ListView):
    model = Service


class ServiceView(DetailView):
    model = Service

class ServiceCreate(CreateView):
    model = Service
    fields = ['name', 'rate']
    success_url = reverse_lazy('service_list')


class ServiceUpdate(UpdateView):
    model = Service
    fields = ['name', 'rate']
    success_url = reverse_lazy('service_list')

class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('service_list')