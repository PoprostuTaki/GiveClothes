from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = 'index.html'


class AddDonationView(TemplateView):
    template_name = 'form.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'
