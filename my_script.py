# DON'T CHANGE Django access code START
# Our Django server is a different space than just running raw Python code.
# The code below gives us access our Django server.
# This lets us query or add data to our Django database.

import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

# from exercises.models import Phonebook
from exercises.models import Phone
from exercises.models import Sport
from exercises.models import Tasklist
from exercises.models import Country
from exercises.models import City
from exercises.models import NBATeam
from exercises.models import NBAAthlete
from exercises.models import Owner
from exercises.models import Pet
from exercises.models import Museums
from exercises.models import Artworks
from exercises.models import Awards
from exercises.models import Winners
from exercises.models import Testings

# # DON'T CHANGE Django access code END
# # blog_data = [{'title':'Bikes, and Bros', 'body':'Young people. Sun burn. Intoxicants of every description'},
# #   {'title': 'Hobbit Holes', 'body': 'You are a person who is deserving of friends and life in general.'},
# #   {'title': 'Drowsy layover', 'body': 'You often make bad decisions whilst travelling;'},
# #   {'title': 'Blood sucking leeches', 'body': 'It was just another day in Nepal, like any other.'}]

# # for blog in blog_data:
# #   Blog.objects.create(title = blog['title'], body = blog['body'])
# #   print(blog)

# Phonebook_data= [{
#   "name": "Benita Leger",
#   "phone": "191-641-4771",
#   "address": "8 Riverside Alley"
# }, {
#   "name": "Eduino Jacobs",
#   "phone": "928-945-4753",
#   "address": "62110 Holmberg Drive"
# }, {
#   "name": "Codi Brooksbie",
#   "phone": "100-688-7702",
#   "address": "3 American Way"
# }, {
#   "name": "Roxanne Ledgerton",
#   "phone": "680-165-3067",
#   "address": "312 Towne Street"
# }, {
#   "name": "Burk Geffen",
#   "phone": "417-284-0620",
#   "address": "9339 Grim Parkway"
# }, {
#   "name": "Birdie Hartles",
#   "phone": "556-244-1277",
#   "address": "393 Portage Way"
# }, {
#   "name": "Analise Flaunders",
#   "phone": "731-991-1730",
#   "address": "0 Portage Drive"
# }, {
#   "name": "Davon Peasby",
#   "phone": "158-539-3390",
#   "address": "7 Holmberg Terrace"
# }, {
#   "name": "Paquito Rubinowitz",
#   "phone": "757-110-6295",
#   "address": "37 Manley Trail"
# }, {
#   "name": "Carlin Stoyle",
#   "phone": "218-314-0186",
#   "address": "47 Morningstar Terrace"
# }, {
#   "name": "Ariadne Conman",
#   "phone": "888-761-3943",
#   "address": "48325 Leroy Crossing"
# }, {
#   "name": "Barbara Cristofolo",
#   "phone": "628-840-3150",
#   "address": "9 Anderson Lane"
# }, {
#   "name": "Dilan O'Rourke",
#   "phone": "304-251-9512",
#   "address": "49 Forest Dale Pass"
# }, {
#   "name": "Robers Durbin",
#   "phone": "161-167-3584",
#   "address": "81612 Crescent Oaks Court"
# }, {
#   "name": "Rossie Darville",
#   "phone": "543-790-9503",
#   "address": "17 Sloan Trail"
# }, {
#   "name": "Melita Brandle",
#   "phone": "991-621-3673",
#   "address": "6 6th Street"
# }, {
#   "name": "Alphard Beardon",
#   "phone": "794-453-3539",
#   "address": "64 2nd Junction"
# }, {
#   "name": "Gamaliel Kedward",
#   "phone": "601-518-5210",
#   "address": "49131 Luster Alley"
# }, {
#   "name": "Xerxes Pirkis",
#   "phone": "612-389-2207",
#   "address": "1 Crowley Drive"
# }, {
#   "name": "Deidre Killough",
#   "phone": "246-344-4179",
#   "address": "53694 Del Mar Street"
# }, {
#   "name": "Sheba Murrhardt",
#   "phone": "925-936-8509",
#   "address": "89885 Southridge Road"
# }, {
#   "name": "Rooney Bilofsky",
#   "phone": "752-711-0322",
#   "address": "8 Mariners Cove Terrace"
# }, {
#   "name": "Valentia Whiterod",
#   "phone": "248-537-1636",
#   "address": "3532 Springs Center"
# }]
# for Phoneboo in Phonebook_data:
#   Phonebook.objects.create(name=Phoneboo['name'], phone=Phoneboo['phone'], address=Phoneboo['address'])
#   print(Phoneboo)


# Write your code below
# Tasklist_data = [{"item": "comb hair", "priority": "2", "is_completed": False}, {"item": "Daily review questions", "priority": "2", "is_completed": False}, {"item": "Cook", "priority": "4", "is_completed": True}, {"item": "Walk dog", "priority": "3", "is_completed": True}, {"item": "Call mom", "priority": "1", "is_completed": True}, {"item": "blah", "priority": "1", "is_completed": True}, {"item": "Study", "priority": "1", "is_completed": True}]
# for list in Tasklist_data:
#   Tasklist.objects.create(item=list["item"], priority=list["priority"], is_completed=list["is_completed"])
#   print(list)

# new_countries = [
#     {  'name': "india", 
#      'population': 1324, 
#      'cities': ["mumbai", "bangalore", 'new dehli']
#     },
#     {  'name': "costa rica", 'population': 4, 'cities': ["san jose", "puntarenas", 'heredia', 'jaco']},
# ]

# loop new_countries:
#   name=india
#   loop cities:
#     1- mumbai 
#     2- bangalore

# for data in new_countries:
#   for city in data['cities']:
#     print(city)
#     # save each city with country object
#     country = Country.objects.get(name=data['name'])
#     City.objects.get_or_create(name=city, country=country)
#     # print(city)


# # other_countries = [{'name': "canada", 'population': 38329563}, {'name': "china", 'population': 1449205531}, {'name': "chile", 'population': 19407929 }]
# # # for list in new_countries:
# # #   Country.objects.create(name=list['name'],population=list['population'])
# # # for data in new_countries:
# # #   country = Country.objects.get(name=data['name'])
# # #   City.objects.create(name=data['cities'],country=country)
# # # print(Country.objects.all())
# # for country in other_countries:
# #   Country.objects.get_or_create(name=country['name'],population=country['population'])
# # print(Country.objects.all())
# other_cities = [
#   {'name': "ontario", 'country': "canada"}, 
#   {'name': "xinjiang", 'country': "china"}, 
#   {"name": "atacama", 'country': "chile"}, 
#   {"name": "yunnan", 'country': "china"}, 
#   {"name": "yukon", 'country': "canada"}, {"name": "gansu", 'country': "china"}, {"name": "quebec", 'country': "canada"}, {"name": "hunan", 'country': "china"}, {"name": "los lagos", 'country': "chile"}, {"name": "antofagasta", 'country': "chile"},]
# # for city in other_cities:
# #   country = Country.objects.get(name=city['country'])
# #   print(country)
# #   City.objects.get_or_create(name=city['name'],country=country)
# print(City.objects.all())

# # done - delete all countries in Country model
# # done - uncomment for loops and try to add the data

# # research "get_or_create()" in django
# # make data structure to add Canada, China, Chile (for loop)
# # loop over cities and store each city

# new_countries = [
#     {  'name': "india", 'population': 1324, 'cities': ["mumbai", "bangalore", 'new dehli']},
#     {  'name': "costa rica", 'population': 5182354, 'cities': ["san jose", "puntarenas", 'heredia', 'jaco']},
# ]
# for list in new_countries:
#   country = Country.objects.create(name=list['name'],population=list['population'])
#   for data in list['cities']:
#     City.objects.create(name=data,country=country)

# players = [
#   {
#     'name':"rockets",
#     'worth': 1650,
#     'athletes': 
#       [
#         "hakeem olajuwon",
#         "moses malone",
#         "yao ming"
#       ]
#   }]
# for data in players:
#   team = NBATeam.objects.create(name=data['name'],worth=data['worth'])
#   for player in data['athletes']:
#     NBAAthlete.objects.create(name=player,team=team)

# pets = [{'name':"susie",'pets':["lola","daisy"]},{'name':"jennifer",'pets':["lucy","luna"]}]
# for list in pets: 
#   owner = Owner.objects.create(name=list['name'])
#   for pet in list['pets']:
#     Pet.objects.create(name=pet,owner=owner)

# list_of_museum = ["The Louvre", "Getty"]
# artworks = [
#   {
#     'The Louvre': [
#       "Mona Lisa", 
#       "Venus de Milo", 
#       "Dying slave"
#     ]
#   },
#   {
#     'Getty': [
#       "Irises",
#       "Lansdowne Herakles"
#     ]
#   }
# ]
# # for list in artworks:
# #   for key, value in list.items():
# #     print("key: ", key)
# #     for art in value:
# #       print("art: ", art)
# for list in list_of_museum:
#   museum = Museums.objects.create(name=list)
# for data in artworks:
#   for key, value in data.items():
#    for art in value:
#      Artworks.objects.create(name=art, museums=museum)

# artworks = [
#   {
#     'name': "The Louvre",
#     'artworks': ["Mona Lisa","Venus de Milo","Dying slave"]
#   },
#   {
#     'name': "Getty",
#     'artworks': ["Irises","Lansdowne Herakles"]
#   }
# ]
# for art in artworks:
#   museum = Museums.objects.create(name=art['name'])
#   for data in art['artworks']:
#     artwork = Artworks.objects.create(name=data,museums=museum)

# # The Louvre - Mona Lisa
# # The Louvre - Venus de Milo
# # The Louvre - Dying slave
# # Getty - Irises
# # Getty - Lansdowne Herakles

# winners = [
#   {
#     'name': "Best Picture",
#     'winner': [
#       {'name': "The Shape of Water",'year': "2018"},
#       {'name': "Moonlight",'year': "2017"},
#       {'name': "Spotlight",'year': "2016"}
#     ]
#   },
#   {
#     'name': "Stanley cup",
#     'winner': [
#       {'name': "Washington Capitals",'year': "2018"},
#       {'name': "Pittsburgh Penguins",'year': "2017"}
#     ]
#   }
# ]
# for winner in winners:
#   award = Awards.objects.create(name=winner['name'])
#   for list in winner['winner']:
#     winners = Winners.objects.create(name=list['name'],year=list['year'],Awards=award)
#     print(winners)

testing = ["jindou","joman"]
for list in testing:
  test = Testings.objects.create(name=list)
  print(test)