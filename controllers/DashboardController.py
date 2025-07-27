from datetime import datetime
from flask import render_template, make_response
from models.AdminModel import get_total_properties, get_properties_by_type, get_properties_by_location
from models.PreferenceModel import get_last_preference
import pdfkit

# Konfigurasi pdfkit dengan wkhtmltopdf
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)


def dashboard():
    total = get_total_properties()
    per_tipe = get_properties_by_type()
    per_lokasi = get_properties_by_location()

    tipe_labels = [tipe for tipe, _ in per_tipe]
    tipe_data = [jumlah for _, jumlah in per_tipe]
    lokasi_labels = [lokasi for lokasi, _ in per_lokasi]
    lokasi_data = [jumlah for _, jumlah in per_lokasi]

    preferensi_raw = get_last_preference()
    if preferensi_raw:
        preferensi = {
            'nama': preferensi_raw[0],
            'user_text': preferensi_raw[1]
        }
    else:
        preferensi = {
            'nama': '—',
            'user_text': '—'
        }
    print("📌 DEBUG: Hasil dari get_last_preference():", preferensi_raw)
    return render_template("admin/dashboard.html",
                           total=total,
                           per_tipe=per_tipe,
                           per_lokasi=per_lokasi,
                           tipe_labels=tipe_labels,
                           tipe_data=tipe_data,
                           lokasi_labels=lokasi_labels,
                           lokasi_data=lokasi_data,
                           preferensi=preferensi)


def dashboard_pdf():
    total = get_total_properties()
    per_tipe = get_properties_by_type()
    per_lokasi = get_properties_by_location()

    tipe_labels = [tipe for tipe, _ in per_tipe]
    tipe_data = [jumlah for _, jumlah in per_tipe]
    lokasi_labels = [lokasi for lokasi, _ in per_lokasi]
    lokasi_data = [jumlah for _, jumlah in per_lokasi]

    preferensi_raw = get_last_preference()

    print("📌 DEBUG: Hasil dari get_last_preference():", preferensi_raw)
    if preferensi_raw:
        print("📌 Panjang tuple preferensi_raw:", len(preferensi_raw))
        for i, val in enumerate(preferensi_raw):
            print(f"  Index {i} → {val}")

    preferensi = {
        'nama': preferensi_raw[0] if len(preferensi_raw) > 0 else '—',
        'tipe': preferensi_raw[2] if len(preferensi_raw) > 2 else '—',
        'harga': preferensi_raw[3] if len(preferensi_raw) > 3 else '—',
        'luas': preferensi_raw[4] if len(preferensi_raw) > 4 else '—',
        'kota': preferensi_raw[5] if len(preferensi_raw) > 5 else '—'
    } if preferensi_raw else {
        'nama': '—', 'tipe': '—', 'harga': '—', 'luas': '—', 'kota': '—'
    }

    html = render_template("admin/dashboard_pdf.html",
                           total=total,
                           per_tipe=per_tipe,
                           per_lokasi=per_lokasi,
                           preferensi=preferensi,
                           now=datetime.now())

    pdf = pdfkit.from_string(html, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=dashboard.pdf'
    return response
