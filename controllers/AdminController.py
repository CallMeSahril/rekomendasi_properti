from datetime import datetime
from flask import render_template, make_response

from models.AdminModel import get_total_properties, get_properties_by_type, get_properties_by_location
from flask import render_template, request, redirect, url_for
from models.AdminModel import get_all_properties, insert_property, get_property_by_id, update_property, delete_property
import os
from werkzeug.utils import secure_filename
from models.AdminModel import get_all_cities
from models.PropertyModel import get_all_property_types
import pdfkit
import locale
from datetime import datetime

# Set locale ke Bahasa Indonesia (pastikan OS mendukung)
try:
    locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')  # Linux/Mac
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'ind')  # Windows fallback

now = datetime.now()
formatted_date = now.strftime('%d %B %Y')  # Contoh: 30 Juli 2025

# Konfigurasi pdfkit dengan wkhtmltopdf
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def cetak_laporan_properti():
    try:
        locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')
    except locale.Error:
        locale.setlocale(locale.LC_TIME, 'ind')
    data = get_all_properties()
    now = datetime.now()


    rendered = render_template(
        "admin/laporan_properti.html", data=data, now=now)

    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
        'margin-top': '10mm',
        'margin-bottom': '10mm',
        'margin-left': '10mm',
        'margin-right': '10mm'
    }

    pdf = pdfkit.from_string(
        rendered, False, configuration=config, options=options)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=laporan_properti.pdf'
    return response


def list_properti():
    data = get_all_properties()
    return render_template('admin/list_properti.html', data=data)


def form_tambah_properti():
    cities = get_all_cities()
    types = get_all_property_types()

    return render_template(
        'admin/form_properti.html',
        action='tambah',
        cities=cities,
        types=types,
        # ← supaya template tidak error saat {% set val = data if data else ['']*12 %}
        data=None
    )


def form_edit_properti(id):
    properti = get_property_by_id(id)
    cities = get_all_cities()
    types = get_all_property_types()  # ← PENTING: kirim data tipe properti ke template
    print("📦 DEBUG: Data Properti yang Diedit:")
    print(properti)
    print("📦 DEBUG: Kota yang Tersedia:")
    print(cities)
    print("📦 DEBUG: Tipe Properti yang Tersedia:")
    print(types)
    return render_template(
        'admin/form_properti.html',
        action='edit',
        data=properti,
        cities=cities,
        types=types
    )


def tambah_properti():
    file = request.files['gambar']
    filename = None

    if file and file.filename != '':
        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
        else:
            return "Hanya file JPG, JPEG, atau PNG yang diperbolehkan!", 400

    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')

    if not latitude or not longitude:
        return "Silakan pilih kota untuk mengisi latitude dan longitude.", 400

    data = (
        request.form['nama_properti'],
        request.form['lokasi'],
        float(latitude),
        float(longitude),
        int(request.form['harga']),
        int(request.form['tipe_id']),

        int(request.form['luas_tanah']),
        int(request.form['luas_bangunan']),
        int(request.form['jumlah_kamar']),
        request.form['deskripsi'],
        filename
    )

    insert_property(data)
    return redirect(url_for('admin_bp.list_properti'))


def update_properti(id):
    file = request.files['gambar']
    filename = request.form.get('gambar_lama')

    if file and file.filename != '':
        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
        else:
            return "Hanya file JPG, JPEG, atau PNG yang diperbolehkan!", 400

    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')

    if not latitude or not longitude:
        return "Silakan pilih kota untuk mengisi latitude dan longitude.", 400

    data = (
        request.form['nama_properti'],
        request.form['lokasi'],
        float(latitude),
        float(longitude),
        int(request.form['harga']),
        int(request.form['tipe_id']),
        int(request.form['luas_tanah']),
        int(request.form['luas_bangunan']),
        int(request.form['jumlah_kamar']),
        request.form['deskripsi'],
        filename
    )

    update_property(id, data)
    return redirect(url_for('admin_bp.list_properti'))


def hapus_properti(id):
    delete_property(id)
    return redirect(url_for('admin_bp.list_properti'))


def dashboard():
    total = get_total_properties()
    per_tipe = get_properties_by_type()
    per_lokasi = get_properties_by_location()

    tipe_labels = [tipe for tipe, _ in per_tipe]
    tipe_data = [jumlah for _, jumlah in per_tipe]
    lokasi_labels = [lokasi for lokasi, _ in per_lokasi]
    lokasi_data = [jumlah for _, jumlah in per_lokasi]

    preferensi_raw = get_last_preference()

    if preferensi_raw and len(preferensi_raw) >= 2:
        nama = preferensi_raw[1].title() if preferensi_raw[1] else '—'
        user_text = preferensi_raw[2] if len(preferensi_raw) > 2 else '—'
    else:
        nama = '—'
        user_text = '—'

    preferensi = {
        'nama': nama,
        'user_text': user_text,
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
        'nama': preferensi_raw[1].title() if len(preferensi_raw) > 1 and preferensi_raw[1] else '—',
        'tipe': preferensi_raw[3] if len(preferensi_raw) > 3 and preferensi_raw[3] else '—',
        'harga': preferensi_raw[4] if len(preferensi_raw) > 4 and preferensi_raw[4] else '—',
        'luas': preferensi_raw[5] if len(preferensi_raw) > 5 and preferensi_raw[5] else '—',
        'kota': preferensi_raw[6] if len(preferensi_raw) > 6 and preferensi_raw[6] else '—',
    } if preferensi_raw else {
        'nama': '—',
        'tipe': '—',
        'harga': '—',
        'luas': '—',
        'kota': '—'
    }

    html = render_template("admin/dashboard_pdf.html",
                           total=total,
                           per_tipe=per_tipe,
                           per_lokasi=per_lokasi,
                           preferensi=preferensi,
                           now=now)

    pdf = pdfkit.from_string(html, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=dashboard.pdf'
    return response
