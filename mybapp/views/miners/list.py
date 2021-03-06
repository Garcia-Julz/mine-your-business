import sqlite3
from django.shortcuts import render
from mybapp.models import Miner
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def miner_list(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            m.id,
            m.city,
            m.user_id,
            u.username,
            u.email
        from mybapp_miner m
        join auth_user u 
        on m.user_id = u.id
        """)

        all_miners = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            mine = Miner()
            mine.id = row["id"]
            mine.city = row["city"]
            mine.user_id = row["user_id"]
            mine.username = row["username"]
            mine.email = row["email"]

            all_miners.append(mine)

    template_name = 'miners/list.html'

    context = {
        'all_miners': all_miners
    }

    return render(request, template_name, context)