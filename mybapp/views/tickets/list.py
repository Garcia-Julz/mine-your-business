import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from mybapp.models import Ticket, IssueType
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def ticket_list(request):
    if request.method == 'GET':
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
                i.cat,
                r.name
                
            from mybapp_ticket t
            JOIN mybapp_issuetype i
            ON t.category_id = i.id
            JOIN mybapp_rig r
            ON t.miner_id = r.id
            """)

            all_tickets = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                ticket = Ticket()
                ticket.id = row['id']
                ticket.title = row['title']
                ticket.comments = row['comments']
                ticket.urgent = row['urgent']
                ticket.name = row['name']
                # ticket.completed = row['completed']
                # ticket.created_at = row['created_at']
                ticket.cat= row['cat']
                # ticket.miner_id = row['miner_id']
                # print('I am ticket', ticket.issue_type_name)

                all_tickets.append(ticket)

        template = 'tickets/list.html'
        context = {
            'all_tickets': all_tickets
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        if "urgent" in form_data:
            urgent = True
        else:
            urgent = False

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO mybapp_ticket
            (
                title, 
                comments, 
                created_at,
                urgent, 
                rig_id
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (form_data['title'], form_data['last_name'],
                form_data['start_date'], urgent, 
                    form_data['rig']))

        return redirect(reverse('mybapp:ticket_list'))