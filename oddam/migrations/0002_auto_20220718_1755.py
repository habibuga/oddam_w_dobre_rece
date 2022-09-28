# Generated by Django 3.2 on 2022-07-18 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oddam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64, verbose_name='nazwa'),
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='nazwa')),
                ('description', models.TextField(max_length=1000, verbose_name='Opis')),
                ('type', models.IntegerField(choices=[(1, 'fundacja'), (2, 'organizacja pozarządowa'), (3, 'zbiórka lokalna')], default=1, verbose_name='typ')),
                ('categories', models.ManyToManyField(to='oddam.Category', verbose_name='Kategoria')),
            ],
        ),
    ]