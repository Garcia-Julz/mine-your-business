import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from ..connection import Connection
from ...models import Ticket
from django.contrib.auth.decorators import login_required


# @login_required
def get_ticket(ticket_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select
                t.id,
                t.title,
                t.comments,
                t.urgent,
                t.created_at,
                t.category_id,
                t.rig_id,
                t.user_id,
                r.name,
                --r.id,
                --i.id,
                i.cat

            FROM mybapp_ticket t
            JOIN mybapp_rig r
            ON t.rig_id = r.id
            JOIN mybapp_issuetype i
            ON i.id = t.category_id
            WHERE t.id = ?
            """, (ticket_id,))

        return db_cursor.fetchone()

def ticket_details(request, ticket_id):
    if request.method == 'GET':
        ticket = get_ticket(ticket_id)

        template = 'tickets/detail.html'
        context = {
            'ticket': ticket
        }

        return render(request, template, {'ticket': ticket})

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM mybapp_ticket
                WHERE id = ?
                """, (ticket_id,))

            return redirect(reverse('mybapp:ticket_list'))