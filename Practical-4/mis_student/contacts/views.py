from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView 
from .models import Contact
from django.urls import reverse_lazy

class ContactList(ListView): 
    model = Contact
    template_name="contact_list.html"
    context_object_name ="contacts"

class ContactDetail(DetailView): 
    model = Contact
    template_name="contact_detail.html"
    context_object_name ="contacts"


class ContactCreate(CreateView): 
    model = Contact
    fields = ('name','email','address','phone')
    template_name="contact_create.html"
    context_object_name ="contacts"
    success_url = reverse_lazy('contact_list')


class ContactUpdate(UpdateView): 
    model = Contact
    fields = ('email','address','phone')
    template_name="contact_form.html"
    context_object_name ="contacts"
    success_url = reverse_lazy('contact_list')


class ContactDelete(DeleteView): 
    model = Contact
    template_name="contact_confirm_delete.html"
    context_object_name ="contacts"
    success_url = reverse_lazy('contact_list')
