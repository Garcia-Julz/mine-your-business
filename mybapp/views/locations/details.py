import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from ..connection import Connection
from ...models import Location
from django.contrib.auth.decorators import login_required


def get_location(location_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select
                l.city,
                l.id
                -- r.name,
                -- r.user_id,
                -- r.location_id

            FROM mybapp_location l
            -- JOIN mybapp_rig r
            -- ON l.id = r.location_id
            WHERE l.id = ?
            """, (location_id,))

        return db_cursor.fetchone()

# @login_required
def location_details(request, location_id):
    if request.method == 'GET':
        location = get_location(location_id)

        template = 'locations/detail.html'
        context = {
            'location': location
        }

        return render(request, template, {'location': location})

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM mybapp_location
                WHERE id = ?
                """, (location_id,))

            return redirect(reverse('mybapp:location_list'))