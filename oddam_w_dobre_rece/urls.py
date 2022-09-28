"""oddam_w_dobre_rece URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from oddam.views import LandingPage, AddDonation, Register, Login, LogoutView, DonationConfirmation, UserProfileView, \
    FoundationPages, NGOPages, CollectionPages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name='start'),
    path('fundacja/<int:page>/', FoundationPages.as_view(), name='foundation'),
    path('ngo/<int:page>/', NGOPages.as_view(), name='ngo'),
    path('zbiorka/<int:page>/', CollectionPages.as_view(), name='collection'),
    path('darowizna/', AddDonation.as_view(), name='add_donation'),
    path('potwierdzenie-darowizny/', DonationConfirmation.as_view(), name='donation_confirmation'),
    path('rejestracja/', Register.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profil/', UserProfileView.as_view(), name='profile'),
]
