import sqlite3
from django.shortcuts import render, redirect, reverse
from mybapp.models import Miner
from ..connection import Connection
from django.contrib.auth.decorators import login_required


# @login_required
def profile_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            current_user = request.user
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    u.id,
                    u.username,
                    u.email,
                    m.city

                FROM  auth_user u
                JOIN mybapp_miner m
                ON m.user_id = u.id
                WHERE u.id = ?
                """,(current_user.id,))

            current_profile = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                profile = Miner()
                profile.id = row["id"]
                profile.username = row["username"]
                profile.email = row["email"]
                profile.city = row["city"]

                current_profile.append(profile)

        template_name = 'profiles/list.html'

        context = {
            'current_profile': current_profile
        }

        return render(request, template_name, context)

    elif request.method == 'POST':
        current_user = request.user
        current_miner_user = Miner.objects.get(user_id=current_user.id)
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO auth_user
            (
                email,
                city,
                id
            )
            VALUES (?, ?, ?)
            """,
            (form_data['email'],
            form_data['city'],
            current_user.id))

        return redirect(reverse('mybapp:profile_list'))