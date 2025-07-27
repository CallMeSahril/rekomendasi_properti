from models.PropertyModel import mysql
# Penting agar hasil fetch dict, bukan tuple
from MySQLdb.cursors import DictCursor


def get_all_properties():
    cur = mysql.connection.cursor(DictCursor)
    cur.execute("""
        SELECT
            p.id,
            p.nama_properti,
            p.lokasi,
            p.latitude,
            p.longitude,
            p.harga,
            p.tipe_id,  -- ✅ tambahkan ini!
            pt.nama AS tipe,
            p.luas_tanah,
            p.luas_bangunan,
            p.jumlah_kamar,
            p.deskripsi,
            p.image_url
        FROM properties p
        LEFT JOIN property_types pt ON p.tipe_id = pt.id
        ORDER BY p.id DESC
    """)
    rows = cur.fetchall()
    cur.close()
    return rows


def get_tipe_name_by_id(tipe_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM property_types WHERE id = %s", (tipe_id,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else "-"


def get_property_by_id(id):
    cur = mysql.connection.cursor(DictCursor)
    cur.execute("""
        SELECT 
            id, nama_properti, lokasi, latitude, longitude, harga, tipe_id,
            luas_tanah, luas_bangunan, jumlah_kamar, deskripsi, image_url
        FROM properties
        WHERE id=%s
    """, (id,))
    data = cur.fetchone()
    cur.close()

    if data:
        print("[DEBUG] Data properti ditemukan:")
        for key, value in data.items():
            print(f"  {key}: {value}")
    else:
        print(f"[DEBUG] Tidak ditemukan properti dengan ID = {id}")

    return data


def insert_property(data):
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO properties (
            nama_properti, lokasi, latitude, longitude, harga, tipe_id,
            luas_tanah, luas_bangunan, jumlah_kamar, deskripsi, image_url
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, data)
    mysql.connection.commit()
    cur.close()


def update_property(id, data):
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE properties SET
            nama_properti=%s, lokasi=%s, latitude=%s, longitude=%s, harga=%s,
            tipe_id=%s, luas_tanah=%s, luas_bangunan=%s, jumlah_kamar=%s,
            deskripsi=%s, image_url=%s
        WHERE id=%s
    """, (*data, id))
    mysql.connection.commit()
    cur.close()


def delete_property(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM properties WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()


def get_all_cities():
    cur = mysql.connection.cursor(DictCursor)
    cur.execute("SELECT nama_kota, latitude, longitude FROM cities")
    cities = cur.fetchall()
    cur.close()
    return cities


def get_total_properties():
    cur = mysql.connection.cursor(DictCursor)
    cur.execute("SELECT COUNT(*) AS total FROM properties")
    result = cur.fetchone()
    cur.close()
    return result['total']


def get_properties_by_type():
    cur = mysql.connection.cursor(DictCursor)
    cur.execute("""
        SELECT pt.nama AS tipe, COUNT(*) AS total
        FROM properties p
        JOIN property_types pt ON p.tipe_id = pt.id
        GROUP BY p.tipe_id
    """)
    result = cur.fetchall()
    cur.close()
    return result


def get_all_property_types():
    cur = mysql.connection.cursor(DictCursor)
    cur.execute("SELECT id, nama FROM property_types ORDER BY nama ASC")
    result = cur.fetchall()
    cur.close()
    return result


def get_properties_by_location():
    cur = mysql.connection.cursor(DictCursor)
    cur.execute(
        "SELECT lokasi, COUNT(*) AS total FROM properties GROUP BY lokasi")
    result = cur.fetchall()
    cur.close()
    return result
