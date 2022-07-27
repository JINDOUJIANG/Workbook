# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero, Animal, Car
from django.urls import reverse



from exercises.models import Summary
from exercises.models import Stock
from exercises.models import Credit_card

# Create your views here.
def superheroes(request):
    
    # code below!
    superheroes = Superhero.objects.filter(is_good=True).filter(is_male = True).filter(name__contains='e')
    # superheroes = Superhero.objects.filter(name__startswith="w")
    
    
    context = { 'superheroes': superheroes }
    return render(request, 'exercises/superhero.html', context)       


def animals(request):
    # animals = None
    
    # code below!
    animals = Animal.objects.filter(birthplace = 'brazil')
    # animals = Animal.objects.all()
    
    context = { 'animals': animals }
    return render(request, 'exercises/animal.html', context)       

def cars(request):
    cars = None
    
    # code below!
    cars = Car.objects.filter(make = 'toyota').filter(year__gte = 1995).order_by('-model')
    # cars = Car.objects.all()
    
    context = { 'cars': cars }
    return render(request, 'exercises/car.html', context)       

    


def templates(request):

    cars = Car.objects.filter(year__gte=2010)

    stocks = Stock.objects.order_by('-market_cap')[:5]
    
    animals = Animal.objects.filter(birthplace='china').filter(name__startswith='g').order_by('-name')

    superheroes = Superhero.objects.filter(is_male=False).filter(rating__gte=7)
    
    
    context = { 'superheroes': superheroes, 'animals': animals, 'cars': cars, 'stocks': stocks }
    return render(request, 'exercises/template.html', context)       

def summary(request):
    

    employees = Summary.objects.all().order_by('-salary')[:5]

    
    context = { 'employees': employees }
    return render(request, 'exercises/summary.html', context)       
    

def submit_form(request):
    context = { }
    return render(request, "exercises/submit_form.html", context)
    
def team_edward(request):
    return HttpResponse(request.POST['message'] + " is a fervent supporter of team edward")
    
def team_jacob(request):
    return HttpResponse(request.POST['message'] + " is a member of team jacob. ROAR!!")

def create_page(request):
    return HttpResponse('hello')

def forrest_gump(request):
    return HttpResponse('life is like a box of chocolates')

def wizard_of_oz(request):
    context = { }
    return render(request, 'exercises/wizard_of_oz.html', context)

def god_father(request):
    return HttpResponse("I'm gonna make him an offer he can't refuse.")

def casablanca(request):
    context = { }
    return render(request, 'exercises/casablanca.html', context)

def credit_cards(request):

    credit_cards = Credit_card.objects.all().order_by('name')
    context = { 'credit_cards': credit_cards }
    return render(request, 'exercises/credit_cards.html', context)