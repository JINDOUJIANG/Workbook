# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import Superhero, Animal, Car, Word
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password

from .models import Quotation
from .models import Credit_card
from .models import Stock
from .models import Blog
from .models import Friend
from .models import Graffiti
from .models import Food
from .models import Phonebook
from .models import Phone
from .models import Sport
from .models import Tasklist

# Create your views here.


def pinboard_project_redo_mainpage(request):
    words = Word.objects.all()
    context = {"words": words}
    return render(request,
                  'pinboard_project_redo/pinboard_project_redo_mainpage.html',
                  context)


def pinboard_project_redo_registerpage(request):
    context = {}
    return render(
        request,
        'pinboard_project_redo/pinboard_project_redo_registerpage.html',
        context)


def pinboard_project_redo_loginpage(request):
    context = {}
    return render(
        request, 'pinboard_project_redo/pinboard_project_redo_loginpage.html',
        context)


def pinboard_project_redo_registeruser(request):
    username = request.POST["Username"]
    email = request.POST["Email address"]
    password = request.POST["Password"]
    user = User.objects.create_user(username=username,
                                    email=email,
                                    password=password)
    login(request, user)
    return HttpResponseRedirect('pinboard_project_redo_dashboardpage')


# CHECK THIS FUNCTION:
def pinboard_project_redo_loginuser(request):
    username = request.POST["Username"]
    password = request.POST["Password"]
    print(username, password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('pinboard_project_redo_dashboardpage')
    else:
        return HttpResponseRedirect('pinboard_project_redo_registerpage')


@login_required
def pinboard_project_redo_changepasswordpage(request):
    context = {}
    return render(
        request,
        'pinboard_project_redo/pinboard_project_redo_changepasswordpage.html',
        context)


@login_required
def pinboard_project_redo_changepassword(request):
    current_password = request.POST["Current password"]
    new_password = request.POST["New password"]
    current_user = request.user
    login_password = current_user.password
    print(login_password)
    # check if current_password is equal to login_password:
    matchcheck = check_password(current_password, login_password)
    if matchcheck:
        current_user.set_password(new_password)
        current_user.save()
        login_password = current_user.password
        login(request, current_user)
        print(login_password)
        return HttpResponseRedirect('pinboard_project_redo_dashboardpage')
    else:
        print("password does not match")
        print(login_password, current_password, new_password)
        return HttpResponseRedirect('pinboard_project_redo_changepasswordpage')
    # # password is: mingren mingren@gmail.com


def pinboard_project_redo_logoutuser(request):
    logout(request)
    return HttpResponseRedirect('pinboard_project_redo_mainpage')


@login_required
def pinboard_project_redo_dashboardpage(request):
    words = Word.objects.all()
    context = {"words": words}
    return render(
        request,
        'pinboard_project_redo/pinboard_project_redo_dashboardpage.html',
        context)


@login_required
def pinboard_project_redo_dashboardsave(request):
    input_word = request.POST["word"]
    # test the type of words:
    # words = Word.objects.all()
    # print(words, "jindou")
    # get the current user:
    current_user = request.user
    # print(current_user)
    user_words = Word.objects.create(word=input_word, user=current_user)
    return HttpResponseRedirect('/pinboard_project_redo_dashboardpage')


def pinboard_page(request):
    logout(request)
    user_quotes = Quotation.objects.all()
    print(user_quotes)
    context = {"user_quotes": user_quotes}
    return render(request, 'exercises/pinboard_page.html', context)


def pinboard_registerpage(request):
    context = {}
    return render(request, 'exercises/pinboard_registerpage.html', context)


# create a situation to avoid the exceptional error
def pinboard_registeruser(request):
    print("see here")
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect('/pinboard_dashboard')


def pinboard_loginpage(request):
    context = {}
    return render(request, 'exercises/pinboard_loginpage.html', context)


def pinboard_loginuser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print('*********************')
        print('user is authenticated')
        print('*********************')
        return HttpResponseRedirect('/pinboard_dashboard')
    else:
        print("**********************")
        print('user not authenticated')
        print("**********************")
        return HttpResponseRedirect('/pinboard_registerpage')


def pinboard_logoutuser(request):
    logout(request)
    print("**********************")
    print(request, "Logged out successfully!")
    print("**********************")
    return HttpResponseRedirect('/pinboard_page')


def pinboard_dashboardsave(request):
    quotations = Quotation.objects.all()
    quote = request.POST["quotation"]
    print("***********************************")
    print(quote)
    print("***********************************")
    current_user = request.user
    print("***********************************")
    print(current_user)
    print("***********************************")
    current_time = datetime.datetime.now()
    print("***********************************")
    print(current_time)
    print("***********************************")
    quotations.create(quote=quote, user=current_user, created_at=current_time)
    return HttpResponseRedirect('/pinboard_dashboard')


@login_required()
def pinboard_dashboard(request):
    quotations = Quotation.objects.all()
    context = {"quotations": quotations}
    print(quotations)
    return render(request, 'exercises/pinboard_dashboard.html', context)


def pinboard_changepasswordpage(request):
    context = {}
    return render(request, 'exercises/pinboard_changepasswordpage.html',
                  context)


# def pinboard_changepassword(request):
#   form_current_password = request.POST["current_password"]
#   print(form_current_password)
#   current_user = User.objects.get(username = request.user)
#   print(current_user.password)
#   matchcheck= check_password(form_current_password, current_user.password)
#   print(matchcheck)
#   if matchcheck:
#     new_password = request.POST["new_password"]
#     current_user.set_password(new_password)
#     current_user.save()
#     updated_user = User.objects.get(username = request.user)
#     print("You changed the password")
#     print(updated_user)
#   else:
#     print("The password you fill out is different than the original one")
#     return HttpResponseRedirect('/pinboard_changepasswordpage')

#   return 6778HttpResponseRedirect('/pinboard_dashboard')


@login_required()
def pinboard_changepassword(request):
    form_current_password = request.POST["current_password"]
    print(form_current_password)
    print(request.user)

    current_user = User.objects.get(username=request.user.username)
    print(current_user.password)
    matchcheck = check_password(form_current_password, current_user.password)
    print(matchcheck)
    new_password = request.POST["new_password"]
    current_user.set_password = new_password
    current_user.save()
    print(current_user.password)
    return HttpResponseRedirect('/pinboard_dashboard')


def public_page(request):
    context = {}
    return render(request, 'exercises/public_page.html', context)


@login_required()
def private_page(request):
    context = {}
    return render(request, 'exercises/private_page.html', context)


def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    # if the user already registered we should redirect to the user registration page
    user = User.objects.create_user(username, email, password)
    # login(request, user)
    return HttpResponseRedirect('/private_page')


def registration_page(request):
    context = {}
    return render(request, 'exercises/registration_page.html', context)


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']

    # Verify user exists in system
    user = authenticate(request, username=username, password=password)
    print("*********************")
    print("*********************")
    print(user)
    print("*********************")
    print("*********************")

    # If user exists in system, user object should have a value. None otherwise.
    if user is not None:
        # Log user into system
        login(request, user)
        print("*********************")
        print('user is authenticated')
        print("*********************")
        # Redirect to private page.
        return HttpResponseRedirect('/private_page')
    else:
        print("**********************")
        print('user not authenticated')
        print("**********************")
        # Redirect back to login page
        return HttpResponseRedirect('/login')


def login_page(request):
    context = {}
    return render(request, 'exercises/login.html', context)


def logout_user(request):
    logout(request)
    print("**********************")
    print('user is logout')
    print("**********************")
    return HttpResponseRedirect('/login')


def update_password(request):
    current_user = request.user
    current_password = request.POST['password']
    print("**********************")
    print("**********************")
    print(current_user.username)
    print("**********************")
    print("**********************")
    # current_user.set_password(current_password)
    print("*******************")
    print('password updated')
    print("*******************")
    current_user.save()
    # u = User.objects.get(username='JJD')
    # u.set_password('JJDpassword')
    # print("*******************")
    # print('password updated')
    # print("*******************")
    # u.save()
    return HttpResponseRedirect('/update_passwordpage')


# changing the password automatically
def update_passwordpage(request):
    context = {}
    return render(request, 'exercises/update_passwordpage.html', context)


def superheroes(request):
    # code below!
    superheroes = Superhero.objects.filter(name="wolverine")

    context = {'superheroes': superheroes}
    return render(request, 'exercises/superhero.html', context)


def animals(request):
    animals = None

    # code below!
    animals = Animal.objects.all()

    context = {'animals': animals}
    return render(request, 'exercises/animal.html', context)


def cars(request):
    cars = None

    # code below!
    cars = Car.objects.all()

    context = {'cars': cars}
    return render(request, 'exercises/car.html', context)


def templates(request):

    superheroes = Superhero.objects.all()

    context = {'superheroes': superheroes}
    return render(request, 'exercises/template.html', context)


def summary(request):

    context = {}
    return render(request, 'exercises/summary.html', context)


def submit_form(request):
    context = {}
    return render(request, "exercises/submit_form.html", context)


def team_edward(request):
    return HttpResponse(request.POST['full_name'] +
                        " is a fervent supporter of team edward")


def team_jacob(request):
    return HttpResponse(request.GET['first_name'] + " " +
                        request.GET['last_name'] +
                        " is a member of team Jacob. ROAR!!")


def bert(request):
    context = {}
    return render(request, "exercises/bert.html", context)


def ernie(request):
    return HttpResponse(request.POST['body_text'])


def timon(request):
    context = {}
    return render(request, 'exercises/timon.html', context)


def pumba(request):
    animal_name = request.POST['animal_name']
    animals = Animal.objects.filter(name__startswith=animal_name)

    context = {'animals': animals}
    return render(request, "exercises/animal_search.html", context)


#form
def superherosearch(request):
    context = {}
    return render(request, 'exercises/superherosearch.html', context)


#Search result
def superhero_search(request):
    superhero_name = request.POST['superhero_name']
    superheroes = Superhero.objects.filter(name__startswith=superhero_name)
    context = {'superhero_name': superhero_name, 'superheroes': superheroes}
    return render(request, "exercises/superhero_search.html", context)


#Detail
def superhero_details(request, superhero_id):
    superhero_details = Superhero.objects.filter(id=superhero_id)
    context = {'superhero_details': superhero_details}
    return render(request, 'exercises/superhero_details.html', context)


def new_template(request):
    context = {}
    return render(request, 'exercises/new_template.html', context)


def animal_page(request):

    animals = Animal.objects.all()
    context = {'animals': animals}
    return render(request, 'exercises/animal_page.html', context)


def credit_cards(request):
    credit_cards = Credit_card.objects.all().order_by('name')
    context = {'credit_cards': credit_cards}
    return render(request, 'exercises/credit_cards.html', context)


def credit_card_details(request, credit_card_id):
    credit_card_details = Credit_card.objects.filter(id=credit_card_id)
    context = {'credit_card_details': credit_card_details}
    return render(request, 'exercises/credit_card_details.html', context)


def forrest_gump(request):
    return HttpResponse('life is like a box of chocolates')


def wizard_of_oz(request):
    context = {}
    return render(request, 'exercises/wizard_of_oz.html', context)


def the_godfather(request):
    return HttpResponse("I'm gonna make him an offer he can't refuse.")


def casablanca(request):
    context = {}
    return render(request, 'exercises/casablanca.html', context)


def stocks(request):
    stocks = Stock.objects.all().order_by('-market_cap')[:5]
    context = {'stocks': stocks}
    return render(request, 'exercises/stocks.html', context)


def tweet(request, username, tweet_id):
    return HttpResponse("user name: " + username + " has tweet_id: " +
                        str(tweet_id))


def new_page(request):
    context = {}
    return render(request, 'exercises/new_page.html', context)


def little_michael(request):
    context = {}
    return render(request, 'exercises/little_michael.html', context)


def css(request):
    context = {}
    return render(request, 'exercises/css.html', context)


def custom(request):
    context = {}
    return render(request, 'exercises/custom.html', context)


def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'exercises/blog.html', context)


def blog_details(request, blog_id):
    blog_details = Blog.objects.filter(id=blog_id)
    context = {'blog_details': blog_details}
    return render(request, 'exercises/blog_details.html', context)


def friend_save(request):
    friend_name = request.POST["full_name"]
    friend = Friend.objects.create(name=friend_name)
    return HttpResponseRedirect("/friend_list")


def friend_list(request):
    all_friends = Friend.objects.all()
    context = {'all_friends': all_friends}
    return render(request, 'exercises/friend_list.html', context)


def delete_friend(request, friend_id):
    friend = Friend.objects.get(id=friend_id)
    friend.delete()
    return HttpResponseRedirect('/friend_list')


def graffiti_save(request):
    graffiti_text = request.POST["textDesEd"]
    graffiti_name = request.POST["text"]
    graffiti = Graffiti.objects.create(name=graffiti_name, text=graffiti_text)
    return HttpResponseRedirect(reverse('exercises:graffiti_list'))


def graffiti_list(request):
    all_graffiti = Graffiti.objects.all()
    context = {'all_graffiti': all_graffiti}
    return render(request, 'exercises/graffiti_list.html', context)


def food_save(request):
    food_name = request.POST["food"]
    food = Food.objects.create(name=food_name)
    return HttpResponseRedirect(reverse('exercises:food_list'))


def food_list(request):
    food_list = Food.objects.all()
    context = {'food_list': food_list}
    return render(request, 'exercises/food_list.html', context)


def update_foodlist(request, food_id):
    update_foodlist = Food.objects.get(id=food_id)
    context = {'update_foodlist': update_foodlist}
    return render(request, 'exercises/update_foodlist.html', context)


def update_save(request, food_id):
    food = request.POST['name']
    update_foodlist = Food.objects.get(id=food_id)
    update_foodlist.name = food
    update_foodlist.save()
    return HttpResponseRedirect(reverse('exercises:food_list'))


def phonebook(request):
    # finish this on Monday
    if 'name' in request.GET:
        search_result = Phone.objects.filter(
            name__startswith=request.GET['name'])
    else:
        search_result = Phone.objects.all().order_by('name')
    context = {'search_result': search_result}
    return render(request, 'exercises/phonebook.html', context)


def updatephonebook(request, phone_id):
    updatephonebook = Phone.objects.get(id=phone_id)
    context = {'updatephonebook': updatephonebook}
    return render(request, 'exercises/updatephonebook.html', context)


def updatephone_save(request, phone_id):
    update_name = request.POST['name']
    update_phone = request.POST['phonenumber']
    update_address = request.POST['address']
    updatephone_save = Phone.objects.get(id=phone_id)
    updatephone_save.name = update_name
    updatephone_save.phonenumber = update_phone
    updatephone_save.address = update_address
    updatephone_save.save()
    return HttpResponseRedirect("/phone_book")


def detailsphonebook(request, phone_id):
    detailsphonebook = Phone.objects.get(id=phone_id)
    context = {'detailsphonebook': detailsphonebook}
    return render(request, 'exercises/detailsphonebook.html', context)


def add_contacts(request):
    context = {}
    return render(request, 'exercises/add_contacts.html', context)


def updatecontacts_save(request):
    updatecontacts_name = request.POST['name']
    updatecontacts_phone = request.POST['phonenumber']
    updatecontacts_address = request.POST['address']
    updatecontacts_save = Phone.objects.create()
    updatecontacts_save.name = updatecontacts_name
    updatecontacts_save.phonenumber = updatecontacts_phone
    updatecontacts_save.address = updatecontacts_address
    updatecontacts_save.save()
    return HttpResponseRedirect('/phone_book')


# def phone_list(request):
#   if 'Search' in request.GET:
#       first_letter = request.GET['Search']
#       print(first_letter)
#       contacts = Phonebook.objects.filter(name__icontains=first_letter) # query filtered contacts based on request.GET['q']
#   else:
#       contacts = Phonebook.objects.all() # query all contacts
#   context = { 'phone_lists': contacts }
#   return render(request, 'exercises/phone_list.html', context)

# def editphonelist_save(request, phonelist_id):
#   name = request.POST['name']
#   phone = request.POST['phone']
#   address = request.POST['address']
#   edit_phonelist = Phonebook.objects.get(id=phonelist_id)
#   edit_phonelist.name = name
#   edit_phonelist.phone = phone
#   edit_phonelist.address = address
#   edit_phonelist.save()
#   return HttpResponseRedirect(reverse('exercises:phone_list'))

# def edit_phonelist(request, phonelist_id):
#   edit_phonelist = Phonebook.objects.get(id=phonelist_id)
#   context = {'edit_phonelist': edit_phonelist}
#   return render(request, 'exercises/edit_phonelist.html', context)

# def details_phone(request, phonelist_id):
#   details_phone = Phonebook.objects.get(id=phonelist_id)
#   context = {'details_phone': details_phone}
#   return render(request, 'exercises/details_phone.html', context)

# def add_phonelist(request):
#   context = {}
#   return render(request, 'exercises/add_phonelist.html', context)

# def addphonelist_save(request):
#   name = request.POST['name']
#   phone = request.POST['phone']
#   address = request.POST['address']
#   add_phonelist = Phonebook.objects.create()
#   add_phonelist.name = name
#   add_phonelist.phone = phone
#   add_phonelist.address = address
#   add_phonelist.save()
#   return HttpResponseRedirect(reverse('exercises:phone_list'))


def athlete_list(request):
    athlete_list = Sport.objects.all().order_by('sport', 'name')
    context = {'athlete_list': athlete_list}
    return render(request, 'exercises/athlete_list.html', context)


def athlete_create(request):
    name = request.POST['name']
    sport = request.POST['sport']
    athlete_create = Sport.objects.create()
    athlete_create.name = name
    athlete_create.sport = sport
    athlete_create.save()
    return HttpResponseRedirect(reverse('exercises:athlete_list'))


def athlete_delete(request, athlete_id):
    athlete_delete = Sport.objects.get(id=athlete_id)
    athlete_delete.delete()
    return HttpResponseRedirect(reverse('exercises:athlete_list'))


def task_list(request):
    if 'task' in request.GET:
        search_result = Tasklist.objects.filter(item=request.GET['task'])
    else:
        search_result = Tasklist.objects.all().order_by('-priority')
    context = {'search_result': search_result}
    return render(request, 'exercises/task_list.html', context)


def add(request):
    name = request.POST['task']
    priority = request.POST['priority']
    add = Tasklist.objects.create()
    add.item = name
    add.priority = priority
    add.save()
    return HttpResponseRedirect(reverse('exercises:task_list'))


def delete(request, item_id):
    tasklist_delete = Tasklist.objects.get(id=item_id)
    tasklist_delete.delete()
    return HttpResponseRedirect(reverse('exercises:task_list'))


def toggle_completion(request, item_id):
    toggle_completion = Tasklist.objects.get(id=item_id)
    toggle_completion.is_completed = not toggle_completion.is_completed
    # if toggle_completion.is_completed == False:
    #   toggle_completion.is_completed = True
    # else:
    #   toggle_completion.is_completed = False

    print(toggle_completion.is_completed)
    toggle_completion.save()
    return HttpResponseRedirect(reverse('exercises:task_list'))


def edit(request, item_id):
    task = Tasklist.objects.get(id=item_id)
    context = {'task': task}
    return render(request, 'exercises/edit.html', context)


def edit_task(request, item_id):
    name = request.POST['task']
    order = request.POST['priority']
    edit_task = Tasklist.objects.get(id=item_id)
    edit_task.item = name
    edit_task.priority = order
    edit_task.save()
    return HttpResponseRedirect(reverse('exercises:task_list'))
