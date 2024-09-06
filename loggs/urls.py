"""Defines URL patterns for loggs."""

from django.urls import path

from . import views

app_name = 'loggs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page that show all loggs.
    path('loggs/', views.loggs, name='loggs'),

    # Page that show a single Logg and it's entries
    path('loggs/<int:logg_id>/', views.logg, name='logg'),

    # Page for adding a new logg
    path('new_logg/', views.new_logg, name='new_logg'),

    # Page for adding a new log in entry.
    path('new_log/<int:logg_id>/', views.new_log, name='new_log'),

    # Page for editing a log in entry
    path('edit_log/<int:log_id>/', views.edit_log, name='edit_log'),
    
    # Path for confirming deleteing a log in entry.
    path('delete_log/<int:log_id>/', views.delete_log, name='delete_log'),

    # Path for confirming deleting an entire Logg
    path('delete_logg/<int:logg_id>/', views.delete_logg, name='delete_logg'),

    
]