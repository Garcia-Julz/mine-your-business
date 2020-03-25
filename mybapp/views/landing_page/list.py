import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from mybapp.models import Ticket, IssueType, Miner
from ..connection import Connection
from django.contrib.auth.decorators import login_required


# @login_required
def sample_view(request):
    current_user = request.user

@login_required
def ticket_list_s(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            current_user = request.user
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
                r.name,
                t.user_id
                
            from mybapp_ticket t
            JOIN mybapp_issuetype i
            ON t.category_id = i.id
            JOIN mybapp_rig r 
            ON r.id = t.rig_id
            WHERE t.user_id = ? AND urgent = 1
            ORDER BY created_at ASC
            LIMIT 3
            """, (current_user.id,))

            all_tickets = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                ticket = Ticket()
                ticket.id = row['id']
                ticket.title = row['title']
                ticket.comments = row['comments']
                ticket.urgent = row['urgent']
                ticket.created_at = row['created_at']
                ticket.cat= row['cat']
                ticket.name = row['name']
                ticket.user_id = row['user_id']
                # *** Might bring this back ***
                # ticket.completed = row['completed']
                # ticket.miner_id = row['miner_id']
                # print('I am ticket', ticket.issue_type_name)

                all_tickets.append(ticket)

        template = 'home/home.html'
        context = {
            'all_tickets': all_tickets
        }

        return render(request, template, context)