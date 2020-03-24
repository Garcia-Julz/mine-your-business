import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from ..connection import Connection
from ...models import Miner
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def get_profile(profile_id):
    with sqlite3.connect(Connection.db_path) as conn:
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
        """, (profile_id,))

        return db_cursor.fetchone()

# @login_required
def profile_details(request, profile_id):
    # print('TEST!', get_profile(profile_id))
    if request.method == 'GET':
        profile = get_profile(profile_id)

        template = 'profiles/detail.html'
        context = {
            'profile': profile
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        # Check if this POST is for editing a project
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            profile = Miner.objects.get(pk=profile_id)
            user = User.objects.get(id=profile.user_id)
            # print('HEllo World', user)
            profile.city = form_data['city']
            user.email = form_data['email']

            profile.save()
            user.save()

            profile = get_profile(profile.id)

            template = 'profiles/detail.html'
            context = {
                'profile': profile
            }

            return render(request, template, context)

            # return redirect(reverse('mybapp:profile', pk=profile.id))

        # NO deleting your profile method in this app yet.

        # if (
        #     "actual_method" in form_data
        #     and form_data["actual_method"] == "DELETE"
        # ):
        #     with sqlite3.connect(Connection.db_path) as conn:
        #         db_cursor = conn.cursor()

        #         db_cursor.execute("""
        #         DELETE FROM mybapp_profile
        #         WHERE id = ?
        #         """, (profile_id,))

        #     return redirect(reverse('mybapp:profile_list'))