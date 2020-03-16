import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from mybapp.models import Ticket, Rig
# from mybapp.models import model_factory
from ..connection import Connection
# from .ticket_details import get_ticket


# @login_required
# def get_locations(request):
#     with sqlite3.connect(Connection.db_path) as conn:
#         current_user = request.user
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         select
#             l.id,
#             l.city

#         FROM mybapp_location l
#         JOIN auth_user u 
#         ON u.id = l.user_id
#         WHERE l.user_id = ?
#         """, (current_user.id,))

#         return db_cursor.fetchall()

@login_required
def location_form(request):
    if request.method == 'GET':
        # location = get_locations(request)
        template = 'locations/form.html'
        # context = {
        #     'all_locations': location
        # }

        return render(request, 
        template)
        # , context)

# def ticket_edit_form(request, ticket_id):

#     if request.method == 'GET':
#         ticket = get_ticket(ticket_id)
#         rig = get_rigs()

#         template = 'tickets/ticket_form.html'
#         context = {
#             'ticket': ticket,
#             'all_rigs': rig
#         }

#         return render(request, template, context)