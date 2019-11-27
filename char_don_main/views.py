from django.contrib.auth import logout
from django.db.models import Count, Sum
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from char_don_main.forms import RegisterForm
from django.views import View
from django.views.generic import TemplateView, FormView
from char_don_main.models import Donation, Institution


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


class AddDonationView(TemplateView):
    template_name = 'form.html'


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)


class LoginView(TemplateView):
    template_name = 'login.html'


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')






