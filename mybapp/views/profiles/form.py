import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from mybapp.models import Ticket
from mybapp.models import IssueType
from mybapp.models import Rig
# from mybapp.models import model_factory
from ..connection import Connection
from .details import get_profile


# @login_required
# def get_rigs(request):
#     with sqlite3.connect(Connection.db_path) as conn:
#         current_user = request.user
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         select
#             r.id,
#             r.name,
#             l.city,
#             r.user_id

#         from mybapp_rig r
#         JOIN mybapp_location l
#         ON r.location_id = l.id
#         WHERE r.user_id = ?
#         """, (current_user.id,))

#         return db_cursor.fetchall()

# def get_issues():
#     with sqlite3.connect(Connection.db_path) as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         select
#             i.id,
#             i.cat
            
#         from mybapp_issuetype i;
#         """)

#         return db_cursor.fetchall()

# @login_required
def profile_form(request):
    if request.method == 'GET':
        template = 'profiles/form.html'
        # context = {
        #     'all_rigs': rig,
        #     'all_issues': issue
        # }

        return render(request, template)

def profile_edit_form(request, profile_id):

    if request.method == 'GET':
        profile = get_profile(profile_id)
        print('hello World!', profile)

        template = 'profiles/form.html'
        context = {
            'profile': profile
        }

        return render(request, template, context) 