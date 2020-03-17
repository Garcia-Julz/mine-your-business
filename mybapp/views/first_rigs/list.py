import sqlite3
from django.shortcuts import render, redirect, reverse
from mybapp.models import Rig, Miner
from ..connection import Connection
from django.contrib.auth.decorators import login_required


def sample_view(request):
    current_user = request.user

@login_required
def rig_list_on(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            current_user = request.user
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
			WHERE r.user_id = ?
            """, (current_user.id,))

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
        current_user = request.user
        current_miner_user = Miner.objects.get(user_id=current_user.id)
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO mybapp_rig
            (
                name, 
                location_id, 
                user_id
            )
            VALUES (?, ?, ?)
            """,
            (form_data['name'], 
            form_data['location'], 
            current_user.id))

        return redirect(reverse('mybapp:home'))