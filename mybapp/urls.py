from django.urls import include, path
from .views import *

app_name = "mybapp"

urlpatterns = [
    path('home/', ticket_list_s, name='home'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name="register"),
    
    path('tickets/', ticket_list, name='ticket_list'),
    path('ticket/form', ticket_form, name='ticket_form'),
    path('rigs/', rig_list, name='rig_list'),
    path('rig/form', rig_form, name='rig_form'),
    path('miners/', miner_list, name='miner_list'),
]