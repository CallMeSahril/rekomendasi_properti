from config import db


def save_client_preference(form):
    cursor = db.cursor()
    sql = """
        INSERT INTO preferensi_klien 
        (nama, kota, latitude, longitude, harga_min, harga_max, luas_tanah, luas_bangunan, tipe_id, kamar_min)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (
        form['nama'],
        form['kota'].split(',')[0],
        float(form['latitude']),
        float(form['longitude']),
        int(form['harga_min']),
        int(form['harga_max']),
        int(form['luas_tanah']),
        int(form['luas_bangunan']),
        int(form['tipe_id']),
        int(form['kamar_min'])
    )
    cursor.execute(sql, data)
    db.commit()
    cursor.close()
