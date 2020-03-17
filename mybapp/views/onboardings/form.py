import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ..connection import Connection


@login_required
def location_form_on(request):
    if request.method == 'GET':
        template = 'onboardings/form.html'
        

        return render(request, 
        template)
        # , context)