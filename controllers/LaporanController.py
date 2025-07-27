from flask import render_template
from datetime import datetime
from models.AdminModel import (
    get_all_properties,
    get_total_properties,
    get_properties_by_type,
    get_properties_by_location
)
from models.PreferenceModel import get_last_preference

# MENU UTAMA LAPORAN


def laporan_menu():
    return render_template("admin/laporan.html")

# LAPORAN TABEL PROPERTI


def laporan_properti():
    data = get_all_properties()
    return render_template("admin/laporan_properti.html", data=data, now=datetime.now)

# LAPORAN PREFERENSI


def laporan_preferensi():
    preferensi_raw = get_last_preference()
    nama, user_text = preferensi_raw if preferensi_raw else ("—", "")

    # Default nilai
    kota = tipe = luas = kamar = '—'

    try:
        parts = user_text.split()
        if len(parts) >= 5:
            kota = f"{parts[0]} {parts[1]}"
            tipe = parts[2].capitalize()
            luas = f"≥ {parts[3].replace('m', '').replace('²', '')} m²"
            kamar = parts[4]
    except:
        pass

    preferensi = {
        'nama': nama,
        'kota': kota,
        'tipe': tipe,
        'harga': '—',
        'luas': luas,
        'kamar': kamar
    }
    return render_template("admin/laporan_preferensi.html", preferensi=preferensi, now=datetime.now)

# LAPORAN STATISTIK


def laporan_statistik():
    total = get_total_properties()
    per_tipe = get_properties_by_type()
    per_lokasi = get_properties_by_location()
    return render_template("admin/laporan_statistik.html", total=total, per_tipe=per_tipe, per_lokasi=per_lokasi, now=datetime.now)

# LAPORAN REKOMENDASI (Dummy Placeholder)


def laporan_rekomendasi():
    hasil = get_all_properties()  # Ganti dengan data hasil rekomendasi asli kalau ada
    return render_template("admin/laporan_rekomendasi.html", hasil=hasil, now=datetime.now)
