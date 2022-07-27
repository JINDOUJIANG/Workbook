# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word + self.user


class Quotation(models.Model):
    quote = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # when new record was created
    created_at = models.DateTimeField(auto_now_add=True)
    # when record was last updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.quote


class Superhero(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    superpower = models.CharField(max_length=100)
    is_good = models.BooleanField()
    is_male = models.BooleanField()
    rating = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=100)
    birthplace = models.CharField(max_length=200)
    is_male = models.BooleanField()

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.make + " " + self.model + " " + str(self.year)


class Stock(models.Model):
    company = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    market_cap = models.FloatField()

    def __str__(self):
        return self.company


class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)
    population = models.IntegerField()

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class NBATeam(models.Model):
    name = models.CharField(max_length=255)
    worth = models.IntegerField()

    def __str__(self):
        return self.name


class NBAAthlete(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(NBATeam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Summary(models.Model):
    employee_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.FloatField()

    def __str__(self):
        return self.employee_name + " " + self.department + " " + str(
            self.salary)


class Credit_card(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    card_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " + str(self.number) + " " + self.card_type


class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=100)

    def __str__(self):
        return self.title + " " + self.body


class Friend(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Graffiti(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.text + " " + self.name


class Food(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Phonebook(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " + self.phone


class Phone(models.Model):
    name = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name + '' + self.phonenumber + '' + self.address


class Sport(models.Model):
    name = models.CharField(max_length=50)
    sport = models.CharField(max_length=50)

    def __str__(self):
        return self.name + '' + self.sport


class Assem(models.Model):
    time = models.CharField(max_length=50)
    joint_angles = models.CharField(max_length=50)

    def __str__(self):
        return self.time + '' + self.joint_angles


class Time_a(models.Model):
    time = models.CharField(max_length=50)
    task = models.CharField(max_length=50)
    state = models.CharField(max_length=10)

    def __str__(self):
        return self.time + '' + self.task + '' + self.state


class Tasklist(models.Model):
    item = models.CharField(max_length=50)
    priority = models.CharField(max_length=10)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + '' + self.priority + '' + self.is_completed


class Owner(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Museums(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Artworks(models.Model):
    name = models.CharField(max_length=50)
    museums = models.ForeignKey(Museums, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Awards(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Winners(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    Awards = models.ForeignKey(Awards, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Testing(models.Model):
    Name = models.CharField(max_length=10)

    def __str__(self):
        return self.Name
