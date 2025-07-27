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

# Konfigurasi pdfkit dengan wkhtmltopdf
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def cetak_laporan_properti():
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

    from models.PreferenceModel import get_last_preference
    preferensi_raw = get_last_preference()
    print("📌 DEBUG: Hasil dari get_last_preference():", preferensi_raw)

    if preferensi_raw and len(preferensi_raw) >= 2:
        preferensi = {
            'nama': preferensi_raw[0],
            'user_text': preferensi_raw[1]
        }
    else:
        preferensi = {
            'nama': '—',
            'user_text': '—'
        }

    return render_template("admin/dashboard.html",
                           total=total,
                           per_tipe=per_tipe,
                           per_lokasi=per_lokasi,
                           tipe_labels=tipe_labels,
                           tipe_data=tipe_data,
                           lokasi_labels=lokasi_labels,
                           lokasi_data=lokasi_data,
                           preferensi=preferensi)
