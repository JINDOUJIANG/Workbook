from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'exercises'


urlpatterns = [
path('pinboard_project_redo_mainpage',views.pinboard_project_redo_mainpage,name='pinboard_project_redo_mainpage'),
path('pinboard_project_redo_registerpage',views.pinboard_project_redo_registerpage,name='pinboard_project_redo_registerpage'),
  path('pinboard_project_redo_loginpage',views.pinboard_project_redo_loginpage,name='pinboard_project_redo_loginpage'),
    path('pinboard_registeruser', views.pinboard_registeruser, name='pinboard_registeruser'), 
  path('pinboard_project_redo_registeruser',views.pinboard_project_redo_registeruser,name='pinboard_project_redo_registeruser'),
path('pinboard_project_redo_loginuser',views.pinboard_project_redo_loginuser,name='pinboard_project_redo_loginuser'),
  path('pinboard_project_redo_dashboardpage',views.pinboard_project_redo_dashboardpage,name='pinboard_project_redo_dashboardpage'),
  path('pinboard_project_redo_dashboardsave',views.pinboard_project_redo_dashboardsave,name='pinboard_project_redo_dashboardsave'),
path('pinboard_project_redo_changepasswordpage',views.pinboard_project_redo_changepasswordpage,name='pinboard_project_redo_changepasswordpage'),
path('pinboard_project_redo_changepassword',views.pinboard_project_redo_changepassword,name='pinboard_project_redo_changepassword'),
    path('pinboard_project_redo_logoutuser',views.pinboard_project_redo_logoutuser,name='pinboard_project_redo_logoutuser'),
    path('pinboard_page', views.pinboard_page, name='pinboard_page'),
    path('pinboard_registerpage', views.pinboard_registerpage, name='pinboard_registerpage'),
    path('pinboard_loginpage', views.pinboard_loginpage, name='pinboard_loginpage'),
    path('pinboard_loginuser', views.pinboard_loginuser, name='pinboard_loginuser'),
    path('pinboard_logoutuser',views.pinboard_logoutuser, name='pinboard_logoutuser'),
    path('pinboard_dashboardsave', views.pinboard_dashboardsave, name='pinboard_dashboardsave'),
    path('pinboard_dashboard', views.pinboard_dashboard, name='pinboard_dashboard'), 
    path('pinboard_changepasswordpage', views.pinboard_changepasswordpage, name='pinboard_changepasswordpage'), 
    path('pinboard_changepassword', views.pinboard_changepassword, name='pinboard_changepassword'),
    path('public_page', views.public_page, name='public_page'),
    path('private_page', views.private_page, name='private_page'),
    path('register_user', views.register_user, name='register_user'),
    path('registration_page', views.registration_page, name='registration_page'),
    path('login_user', views.login_user, name='login_user'),
    path('login', views.login_page, name='login'), 
    path('logout', views.logout_user, name='logout'),
    path('update_passwordpage', views.update_passwordpage, name='update_passwordpage'),
    path('update_password', views.update_password, name='update_password'),
    path('', views.superheroes, name='superheroes'),
    path('animals', views.animals, name='animals'),
    path('cars', views.cars, name='cars'),
    path('templates', views.templates, name='templates'),
    path('summary', views.summary, name='summary'),
    
    path('submit_form', views.submit_form, name='submit_form'),
    path('team_edward', views.team_edward, name='team_edward'),
    path('team_jacob', views.team_jacob, name='team_jacob'),
    
    # add new capture here
   
    path('new_template', views.new_template, name='new_template'),
    path('animal_page', views.animal_page, name='animal_page'),
    path('new_credit_card_link', views.credit_cards, name='credit_cards'),
    # path('credit_cards', views.credit_cards, name='credit_cards'),
    path('new_credit_card_details/<int:credit_card_id>', views.credit_card_details, name="credit_card_details"),
    # path('credit_card_details/<int:credit_card_id>', views.credit_card_details, name="credit_card_details"),
    #  credit_card_details/25
    
    path('forrest_gump', views.forrest_gump, name='forrest_gump'),
    path('wizard_of_oz', views.wizard_of_oz, name='wizard_of_oz'),
    path('the_godfather', views.the_godfather, name='the_godfather'),
    path('casablanca', views.casablanca, name='casablanca'),
    path('stocks', views.stocks, name='stocks'),
    path('<str:username>/status/<int:tweet_id>', views.tweet, name='tweet'),
    path('new_page', views.new_page, name='new_page'),
    path('little_michael', views.little_michael, name='little_michael'),
    path('css', views.css, name='css'),
    path('custom', views.custom, name='custom'),
    path('blog', views.blogs, name='blogs'),
    path('blog_details/<int:blog_id>', views.blog_details, name='blog_details'),
    path('bert', views.bert, name='bert'),
    path('ernie', views.ernie, name='ernie'),
    path('timon', views.timon, name='timon'),
    path('animal_search', views.pumba, name='pumba'),
    
    #Search result
    path('results_superheroes', views.superhero_search, name='superhero_search'),
    #form
    path('superherosearch', views.superherosearch, name='superherosearch'),
    #detail
    path('details_superhero/<int:superhero_id>', views.superhero_details, name='superhero_details'),
    
    path('friend_list', views.friend_list, name='friend_list'),
    path('friend_save', views.friend_save, name='friend_save'),
    path('delete_friend/<int:friend_id>', views.delete_friend, name='delete_friend'),

    path('graffiti', views.graffiti_list, name='graffiti_list'),
    path('graffiti_save', views.graffiti_save, name='graffiti_save'),

    path('food_list', views.food_list, name='food_list'),
    path('food_save', views.food_save, name='food_save'),
    path('update_foodlist/<int:food_id>', views.update_foodlist, name='update_foodlist'),
    path('update_save/<int:food_id>', views.update_save, name='update_save'),
    # path('phone_list', views.phone_list, name='phone_list'),
    # path('edit_phonelist/<int:phonelist_id>', views.edit_phonelist,    name='edit_phonelist'),
    # path('editphonelist_save/<int:phonelist_id>', views.editphonelist_save, name='editphonelist_save'),
    # path('details_phone/<int:phonelist_id>', views.details_phone, name='details_phone'),
    # path('add_phonelist', views.add_phonelist, name='add_phonelist'), 
    # path('addphonelist_save', views.addphonelist_save, name='addphonelist_save'), 
    path('phone_book', views.phonebook, name='phonebook'),
    path('update_phonebook/<int:phone_id>', views.updatephonebook, name='updatephonebook'),
    path('details_phonebook/<int:phone_id>', views.detailsphonebook, name='detailsphonebook'),
    path('updatephone_save/<int:phone_id>', views.updatephone_save, name='updatephone_save'),
    path('add_contacts', views.add_contacts, name='add_contacts'),
    path('updatecontacts_save', views.updatecontacts_save, name='updatecontacts_save'),
    path('athlete_list', views.athlete_list, name='athlete_list'),
    path('athlete_create', views.athlete_create, name='athlete_create'),
    path('athlete_delete/<int:athlete_id>', views.athlete_delete, name='athlete_delete'), 
    path('custom_task_list', views.task_list, name='task_list'),
    path('custom_add', views.add, name='add'),
    path('custom_delete/<int:item_id>', views.delete, name='delete'),
    path('custom_toggle_completion/<int:item_id>', views.toggle_completion, name='toggle_completion'),
    path('custom_edit/<int:item_id>', views.edit, name='edit'),
    path('custom_edit_task/<int:item_id>', views.edit_task, name='edit_task'),
    
    
]
