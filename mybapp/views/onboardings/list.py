import sqlite3
from django.shortcuts import render, redirect, reverse
from mybapp.models import Location, Miner
from ..connection import Connection
from django.contrib.auth.decorators import login_required


def sample_view(request):
    current_user = request.user

@login_required
def location_list_on(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            current_user = request.user
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                l.city,
                l.user_id

            FROM mybapp_location l
            JOIN auth_user u
            ON u.id = l.user_id
			WHERE l.user_id = ?
            """, (current_user.id,))

            all_locations = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                loc = Location()
                loc.city = row["city"]
                loc.user_id = row["user_id"]
                # loc.id = row["id"]
                # loc.id = row["id"]

                all_locations.append(loc)

        template_name = 'onboardings/list.html'

        context = {
            'all_locations': all_locations
        }

        return render(request, template_name, context)

    elif request.method == 'POST':
        current_user = request.user
        current_miner_user = Miner.objects.get(user_id=current_user.id)
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO mybapp_location
            (
                city,
                user_id
            )
            VALUES (?, ?)
            """,
            (form_data['city'],
            current_user.id))

        return redirect(reverse('mybapp:rig_form_on'))