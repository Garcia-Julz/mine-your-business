import sqlite3
from django.shortcuts import render
from mybapp.models import Ticket
from ..connection import Connection
# from django.contrib.auth.decorators import login_required


# @login_required
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
                t.completed,
                t.created_at,
                t.issue_type_name_id,
                t.miner_id,
                t.rig_id
            from mybapp_ticket b
            """)

            all_tickets = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                ticket = Ticket()
                ticket.id = row['id']
                ticket.title = row['title']
                ticket.comments = row['comments']
                ticket.urgent = row['urgent']
                ticket.completed = row['completed']
                ticket.created_at = row['created_at']
                ticket.issue_type_name = row['issue_type_name']
                ticket.miner_id = row['miner_id']
                ticket.rig_id = row['rig_id']

                all_tickets.append(ticket)

        template = 'tickets/list.html'
        context = {
            'all_tickets': all_tickets
        }

        return render(request, template, context)