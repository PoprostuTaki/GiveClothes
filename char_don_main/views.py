from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView
from django.db.models import Count, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy

from char_don_main.forms import RegisterForm
from django.views import View
from django.views.generic import FormView
from char_don_main.models import Donation, Institution, Category


class LandingPageView(View):
    def get(self, request):
        # wyświetlanie liczników instytucji i ilości worków:
        institution_count = Donation.objects.aggregate(institution_count=Count('institution', distinct=True))
        quantity = Donation.objects.aggregate(quantity_sum=Sum('quantity'))
        # paginacja:
        type_fun_list = Institution.objects.filter(type='FUN')
        type_org_list = Institution.objects.filter(type='ORG')
        type_lok_list = Institution.objects.filter(type='LOK')
        paginator1 = Paginator(type_fun_list, 5)  # Show 5 contacts per page
        paginator2 = Paginator(type_org_list, 5)  # Show 5 contacts per page
        paginator3 = Paginator(type_lok_list, 5)  # Show 5 contacts per page
        page = request.GET.get('page')
        type_fun = paginator1.get_page(page)
        type_org = paginator2.get_page(page)
        type_lok = paginator3.get_page(page)
        return render(request, 'index.html', {'institution_count': institution_count['institution_count'],
                                              'quantity': quantity['quantity_sum'],
                                              'type_fun': type_fun, 'type_org': type_org, 'type_lok': type_lok})


class AddDonationView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, 'institutions': institutions})


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('custom_login')

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)


# class SystemPasswordResetView(PasswordResetView):
#     template_name = 'registration/password_reset_form.html'
#     success_url = reverse_lazy('password_reset_done')
#
# class SystemPasswordResetDoneView(PasswordResetDoneView):
#     template_name = 'registration/password_reset_done.html'


class CustomLoginView(LoginView):
    def form_invalid(self, form):
        username = form.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            return super(CustomLoginView, self).form_invalid(form)
        else:
            return redirect(reverse_lazy('register'))






