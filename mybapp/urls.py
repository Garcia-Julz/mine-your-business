from django.urls import include, path
from .views import *

app_name = "mybapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('', home, name='home'),
    path('tickets/', ticket_list, name='tickets'),
    path('miners/', miner_list, name='miners'),
    path('rigs/', rig_list, name='rigs'),
]