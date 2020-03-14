import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from mybapp.models import Ticket
from mybapp.models import Rig
# from mybapp.models import model_factory
from ..connection import Connection
# from .ticket_details import get_ticket


def get_rigs():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            r.id,
            r.name,
            l.city
        from mybapp_rig r
        JOIN mybapp_location l
        ON r.location_id = l.id
        """)

        return db_cursor.fetchall()

@login_required
def ticket_form(request):
    if request.method == 'GET':
        rig = get_rigs()
        template = 'tickets/ticket_form.html'
        context = {
            'all_rigs': rig
        }

        return render(request, template, context)

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