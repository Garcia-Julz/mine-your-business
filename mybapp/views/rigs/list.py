import sqlite3
from django.shortcuts import render, redirect, reverse
from mybapp.models import Rig
from ..connection import Connection
# from django.contrib.auth.decorators import login_required


# @login_required
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
                r.miner_id,
                u.username

            from mybapp_rig r
            join auth_user u 
            on r.id = u.id
            """)

            all_rigs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                rig = Rig()
                rig.id = row["id"]
                rig.name = row["name"]
                rig.location = row["location"]

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