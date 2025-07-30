from flask_mysqldb import MySQL
import numpy as np
from MySQLdb.cursors import DictCursor

mysql = MySQL()


def init_mysql(app):
    app.config.from_pyfile('config.py')
    mysql.init_app(app)
    return mysql


def fetch_all_properties():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM properties")
    result = cursor.fetchall()
    cursor.close()
    return result


def fetch_all_cities():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama_kota, latitude, longitude FROM cities")
    result = cursor.fetchall()
    cursor.close()
    return result


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # radius bumi dalam km
    lat1, lon1, lat2, lon2 = map(lambda x: np.radians(float(x)), [
                                 lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    return R * c


def get_all_property_types():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nama FROM property_types")
    result = [row[0] for row in cursor.fetchall()]  # ['Rumah', 'Tanah', ...]
    cursor.close()
    return result
