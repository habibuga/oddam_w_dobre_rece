from django.db import models

ORGANIZATIONS = (
    (1, "fundacja"),
    (2, "organizacja pozarządowa"),
    (3, "zbiórka lokalna"),
)


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name="nazwa")


class Institution(models.Model):
    name = models.CharField(max_length=64, verbose_name="nazwa")
    description = models.TextField(max_length=1000, verbose_name='Opis')
    type = models.IntegerField(choices=ORGANIZATIONS, default=1, verbose_name="typ")
    categories = models.ManyToManyField(Category, verbose_name='Kategoria')
