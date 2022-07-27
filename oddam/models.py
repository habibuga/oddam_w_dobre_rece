from django.contrib.auth.models import User
from django.db import models

ORGANIZATIONS = (
    (1, "fundacja"),
    (2, "organizacja pozarządowa"),
    (3, "zbiórka lokalna"),
)


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name="nazwa")

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=64, verbose_name="nazwa")
    description = models.TextField(max_length=1000, verbose_name='opis')
    type = models.IntegerField(choices=ORGANIZATIONS, default=1, verbose_name="typ")
    categories = models.ManyToManyField(Category, verbose_name='kategoria')

    def category_names(self):
        return ', '.join([c.name for c in self.categories.all()])


class Donation(models.Model):
    quantity = models.IntegerField(verbose_name="liczba worków")
    categories = models.ManyToManyField(Category, verbose_name='kategoria')
    institution = models.ForeignKey(Institution, verbose_name="organizacja", on_delete=models.CASCADE)
    address = models.CharField(max_length=256, verbose_name="adres")
    phone_number = models.IntegerField(verbose_name="numer telefonu")
    city = models.CharField(max_length=64, verbose_name="miasto")
    zip_code = models.CharField(max_length=6, verbose_name="kod pocztowy")
    pick_up_date = models.DateField(verbose_name="data odbioru")
    pick_up_time = models.TimeField(verbose_name="godzina odbioru")
    pick_up_comment = models.CharField(max_length=500, verbose_name="komentarz")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="darczyńca")
