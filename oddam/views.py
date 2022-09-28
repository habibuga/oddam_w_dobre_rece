from django.shortcuts import render
from django.views import View
from .models import Donation, Institution


class LandingPage(View):
    def get(self, request):
        bags = 0
        for donation in Donation.objects.all():
            bags += donation.quantity
        charities_number = Institution.objects.count()
        charities_org = Institution.objects.all()
        ctx = {
            "bags_num": bags,
            "charity_num": charities_number,
            "charities": charities_org
        }
        return render(request=request, template_name='index.html', context=ctx)


class AddDonation(View):
    def get(self, request):
        return render(request=request, template_name='form.html')


class Register(View):
    def get(self, request):
        return render(request=request, template_name='register.html')


class Login(View):
    def get(self, request):
        return render(request=request, template_name='login.html')
