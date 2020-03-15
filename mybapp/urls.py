from django.urls import include, path
from .views import *

app_name = "mybapp"

urlpatterns = [
    path('', home, name='home'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name="register"),
    
    path('tickets/', ticket_list, name='ticket_list'),
    path('miners/', miner_list, name='miner_list'),
    path('rigs/', rig_list, name='rig_list'),
    path('ticket/form', ticket_form, name='ticket_form'),
]