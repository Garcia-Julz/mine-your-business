from django.urls import include, path
from .views import *

app_name = "mybapp"

urlpatterns = [
    # User actions
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name="register"),
    # New user onboarding
    path('onboardings/', location_list_on, name='location_list_on'),
    path('onboarding/form', location_form_on, name='location_form_on'),
    path('firstrig/', rig_list_on, name='rig_list_on'),
    path('firstrig/form', rig_form_on, name='rig_form_on'),
    # Home
    path('home/', ticket_list_s, name='home'),
    # Lists
    path('locations/', location_list, name='location_list'),
    path('rigs/', rig_list, name='rig_list'),
    path('tickets/', ticket_list, name='ticket_list'),
    path('profiles/', profile_list, name='profile_list'),
    # Forms
    path('location/form', location_form, name='location_form'),
    path('rig/form', rig_form, name='rig_form'),
    path('ticket/form', ticket_form, name='ticket_form'),
    path('profile/form', profile_form, name='profile_form'),
    # Details
    path('locations/<int:location_id>/', location_details, name='location'),
    path('rigs/<int:rig_id>/', rig_details, name='rig'),
    path('tickets/<int:ticket_id>/', ticket_details, name='ticket'),
    path('miners/', miner_list, name='miner'),
    path('profiles/<int:profile_id>/', profile_details, name='profile'),
    # Edit forms
    path('locations/<int:location_id>/form/', location_edit_form, name='location_edit_form'),
    path('lrigs/<int:rig_id>/form/', rig_edit_form, name='rig_edit_form'),
    path('tickets/<int:ticket_id>/form/', ticket_edit_form, name='ticket_edit_form'),
    path('profiles/<int:profile_id>/form/', profile_edit_form, name='profile_edit_form'),

]