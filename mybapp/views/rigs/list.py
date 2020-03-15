import sqlite3
from django.shortcuts import render, redirect, reverse
from mybapp.models import Rig
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def rig_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                r.id,
                r.name,
                r.location_id,
                r.user_id,
                u.username,
                l.city

            FROM mybapp_rig r
            JOIN auth_user u
            ON r.user_id = u.id
            JOIN mybapp_location l 
            ON r.location_id = l.id
            """)

            all_rigs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                rig = Rig()
                rig.id = row["id"]
                rig.name = row["name"]
                rig.location_id = row["location_id"]
                rig.user_id = row["user_id"]
                rig.username = row["username"]
                rig.city = row["city"]

                all_rigs.append(rig)

        template_name = 'rigs/list.html'

        context = {
            'all_rigs': all_rigs
        }

        return render(request, template_name, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO mybapp_rig
            (
                name, location_id
            )
            VALUES (?, ?)
            """,
            (form_data['name'], form_data['location_id']))

        return redirect(reverse('mybapp:rigs'))