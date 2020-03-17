import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from ..connection import Connection
from ...models import Rig
from django.contrib.auth.decorators import login_required


# @login_required
def get_rig(rig_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select
                r.id,
                r.name,
                r.user_id,
                r.location_id,
                l.city,
                l.id

            FROM mybapp_rig r
            JOIN mybapp_location l
            ON r.location_id = l.id
            WHERE r.id = ?
            """, (rig_id,))

        return db_cursor.fetchone()

def rig_details(request, rig_id):
    if request.method == 'GET':
        rig = get_rig(rig_id)

        template = 'rigs/detail.html'
        context = {
            'rig': rig
        }

        return render(request, template, {'rig': rig})

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM mybapp_rig
                WHERE id = ?
                """, (rig_id,))

            return redirect(reverse('mybapp:rig_list'))