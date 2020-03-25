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
                t.completed,
                t.created_at,
                t.category_id,
                t.rig_id,
                t.user_id,
                r.name,
                i.cat

            FROM mybapp_ticket t
            JOIN mybapp_rig r
            ON t.rig_id = r.id
            JOIN mybapp_issuetype i
            ON i.id = t.category_id
            WHERE t.id = ?
            """, (ticket_id,))

        return db_cursor.fetchone()

# @login_required
def ticket_details(request, ticket_id):
    # print('TEST!', get_ticket(ticket_id))
    if request.method == 'GET':
        ticket = get_ticket(ticket_id)

        template = 'tickets/detail.html'
        context = {
            'ticket': ticket
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        # Check if this POST is for editing a project
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            if "completed" in form_data:
                completed = True
            else:
                completed = False

            if "urgent" in form_data:
                urgent = True
            else:
                urgent = False

            ticket = Ticket.objects.get(pk=ticket_id)

            ticket.title = form_data['title']
            ticket.comments = form_data['comments']
            ticket.created_at = form_data['created_at']
            ticket.urgent = urgent
            ticket.completed = completed
            ticket.rig_id = form_data['rig']
            ticket.category_id = form_data['issue']

            ticket.save()
            return redirect(reverse('mybapp:ticket_list'))

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