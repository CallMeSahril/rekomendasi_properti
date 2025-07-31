
from models.PropertyModel import mysql
from datetime import datetime
from datetime import datetime


def simpan_preferensi(nama, preferensi):
    now = datetime.now()  # Tambahkan baris ini
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO preferensi_klien (nama, user_text, created_at)
        VALUES (%s, %s, %s)
    """, (nama, preferensi, now))

    mysql.connection.commit()
    cursor.close()


def get_last_preference():
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT nama, user_text
        FROM preferensi_klien
        ORDER BY id DESC
        LIMIT 1
    """)
    result = cursor.fetchone()
    cursor.close()
    return result


def get_all_preferences():
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT id, nama, user_text, created_at
        FROM preferensi_klien
        ORDER BY created_at DESC
    """)
    result = cursor.fetchall()
    cursor.close()
    return result


def get_all_preferences_A():
    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT nama, user_text FROM preferensi_klien ORDER BY id ASC")
    result = cursor.fetchall()
    cursor.close()
    return result
