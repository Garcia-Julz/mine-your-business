from django.urls import include, path
from .views import *

app_name = "mybapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name="register"),

    path('home/', ticket_list_s, name='home'),
    
    path('locations/', location_list, name='location_list'),
    path('location/form', location_form, name='location_form'),
    path('onboardings/', location_list_on, name='location_list_on'),
    path('onboarding/form', location_form_on, name='location_form_on'),
    path('tickets/', ticket_list, name='ticket_list'),
    path('ticket/form', ticket_form, name='ticket_form'),
    path('tickets/<int:ticket_id>/', ticket_details, name='ticket'),
    path('rigs/', rig_list, name='rig_list'),
    path('firstrig/', rig_list_on, name='rig_list_on'),
    path('firstrig/form', rig_form_on, name='rig_form_on'),
    path('rigs/<int:rig_id>/', rig_details, name='rig'),
    path('rig/form', rig_form, name='rig_form'),
    path('miners/', miner_list, name='miner_list'),
]