from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from .forms import NewUserForm
from .models import Donation, Institution


class LandingPage(View):
    def get(self, request):
        bags = 0
        for donation in Donation.objects.all():
            bags += donation.quantity
        charities_number = Institution.objects.count()
        charities_found = Institution.objects.filter(type=1)
        paginator_found = Paginator(charities_found, 5)
        charities_ngo = Institution.objects.filter(type=2)
        paginator_ngo = Paginator(charities_ngo, 5)
        charities_coll = Institution.objects.filter(type=3)
        paginator_coll = Paginator(charities_coll, 5)

        page = request.GET.get('page')
        charities_found_p = paginator_found.get_page(page)
        charities_ngo_p = paginator_ngo.get_page(page)
        charities_coll_p = paginator_coll.get_page(page)
        ctx = {
            "bags_num": bags,
            "charity_num": charities_number,
            "charities_found": charities_found_p,
            "charities_ngo": charities_ngo_p,
            "charities_coll": charities_coll_p
        }
        return render(request=request, template_name='index.html', context=ctx)


class AddDonation(View):
    def get(self, request):
        return render(request=request, template_name='form.html')


class Register(View):
    def get(self, request):
        form = NewUserForm()
        ctx = {
            "form": form,
        }
        return render(request=request, template_name='register.html', context=ctx)

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')
        else:
            form.add_error(None, 'Wprowadź poprwane dane!')
            ctx = {
                "form": form,
            }
            return render(request=request, template_name="register.html", context=ctx)


class Login(View):
    def get(self, request):
        return render(request=request, template_name='login.html')
