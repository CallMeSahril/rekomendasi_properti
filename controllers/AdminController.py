from datetime import datetime
from flask import render_template, make_response
from collections import Counter
import re

from models.AdminModel import get_total_properties, get_properties_by_type, get_properties_by_location
from flask import render_template, request, redirect, url_for
from models.AdminModel import get_all_properties, insert_property, get_property_by_id, update_property, delete_property
import os
from werkzeug.utils import secure_filename
from models.AdminModel import get_all_cities
from models.PropertyModel import get_all_property_types, fetch_all_properties
import pdfkit
import locale
from datetime import datetime
from models.PreferenceModel import get_last_preference, get_all_preferences_A

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


def parse_user_text(user_text):
    user_text = user_text.lower()
    tipe_list = [tipe.lower() for tipe in get_all_property_types()]
    lokasi_list = ['jakarta timur', 'jakarta selatan',
                   'jakarta barat', 'jakarta pusat', 'jakarta utara']

    tipe = next((t for t in tipe_list if t in user_text), None)
    lokasi = next((l for l in lokasi_list if l in user_text), None)

    angka = re.findall(r'\b\d+\b', user_text)
    harga = f"Rp {int(angka[0]) * 1_000_000:,}".replace(",",
                                                        ".") if angka else '—'

    if len(angka) >= 2:
        luas = f"{angka[1]} m²"
    elif "minimalis" in user_text:
        luas = "≤ 100 m²"
    else:
        luas = "—"

    return {
        "tipe": tipe.title() if tipe else "—",
        "harga": harga,
        "luas": luas,
        "lokasi": lokasi.title() if lokasi else "—"
    }


def extract_summary(preference_rows):
    tipe_counter = Counter()
    lokasi_counter = Counter()
    harga_list = []
    luas_list = []

    for nama, user_text in preference_rows:
        parsed = parse_user_text(user_text)

        if parsed['tipe'] != '—':
            tipe_counter[parsed['tipe']] += 1
        if parsed['lokasi'] != '—':
            lokasi_counter[parsed['lokasi']] += 1
        if parsed['harga'] != '—':
            angka = re.findall(r'\d+', parsed['harga'].replace(".", ""))
            if angka:
                harga_list.append(int(angka[0]))
        if parsed['luas'] != '—' and 'm²' in parsed['luas']:
            luas = re.findall(r'\d+', parsed['luas'])
            if luas:
                luas_list.append(int(luas[0]))

    tipe_favorit = tipe_counter.most_common(1)[0][0] if tipe_counter else '—'
    harga_favorit = f"Rp {sum(harga_list)//len(harga_list):,}".replace(",",
                                                                       ".") if harga_list else '—'
    luas_favorit = f"{sum(luas_list)//len(luas_list)} m²" if luas_list else '—'
    lokasi_favorit = lokasi_counter.most_common(
        1)[0][0] if lokasi_counter else '—'

    return {
        'tipe': tipe_favorit,
        'harga': harga_favorit,
        'luas': luas_favorit,
        'lokasi': lokasi_favorit
    }


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


def dashboard():
    all_properties = fetch_all_properties()
    total = len(all_properties)

    # Hitung per_tipe dan per_lokasi secara manual
    tipe_counter = Counter()
    lokasi_counter = Counter()

    for row in all_properties:
        tipe_id = row[12]  # tipe_id = kolom ke-13 (index 12)
        lokasi = row[2]    # lokasi = kolom ke-3 (index 2)

        tipe_list = get_all_property_types()
        tipe_name = tipe_list[tipe_id -
                              1] if 0 < tipe_id <= len(tipe_list) else "Tidak Diketahui"

        tipe_counter[tipe_name] += 1
        lokasi_counter[lokasi] += 1

    # Konversi ke format yang biasa dipakai di template
    # [('Rumah', 3), ('Tanah', 2)]
    per_tipe = list(tipe_counter.items())
    # [('Jakarta Timur', 4), ...]
    per_lokasi = list(lokasi_counter.items())

    tipe_labels = list(tipe_counter.keys())
    tipe_data = list(tipe_counter.values())
    lokasi_labels = list(lokasi_counter.keys())
    lokasi_data = list(lokasi_counter.values())

    # Preferensi (nama & user_text tetap ambil dari preferensi terakhir)
    all_preferences = get_all_preferences_A()
    if all_preferences:
        nama_terakhir = all_preferences[-1][0].title()
        user_text_terakhir = all_preferences[-1][1]
        summary = extract_summary(all_preferences)

        # lokasi = index ke-2
        lokasi_list = list(sorted({row[2] for row in all_properties}))

        preferensi = {
            'nama': nama_terakhir,
            'user_text': user_text_terakhir,
            'tipe': ', '.join(get_all_property_types()) or '—',
            'harga': summary['harga'],
            'luas': summary['luas'],
            'kota': ', '.join(lokasi_list) or '—'
        }
    else:
        preferensi = {
            'nama': '—',
            'user_text': '—',
            'tipe': ', '.join(get_all_property_types()) or '—',
            'harga': '—',
            'luas': '—',
            'kota': '—'
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


def dashboard_pdf():
    all_properties = fetch_all_properties()
    total = len(all_properties)

    tipe_counter = Counter()
    lokasi_counter = Counter()
    tipe_list = get_all_property_types()

    for row in all_properties:
        lokasi = row[2]
        tipe_id = row[12]
        tipe_name = tipe_list[tipe_id - 1] if isinstance(
            tipe_id, int) and 0 < tipe_id <= len(tipe_list) else 'Tidak Diketahui'
        tipe_counter[tipe_name] += 1
        lokasi_counter[lokasi] += 1

    per_tipe = list(tipe_counter.items())
    per_lokasi = list(lokasi_counter.items())
    all_preferences = get_all_preferences_A()

    if all_preferences:
        nama_terakhir = all_preferences[-1][0].title()
        user_text_terakhir = all_preferences[-1][1]
        summary = extract_summary(all_preferences)
        lokasi_list = list(sorted({row[2] for row in all_properties}))

        preferensi = {
            'nama': nama_terakhir,
            'user_text': user_text_terakhir,
            'tipe': ', '.join(tipe_list) or '—',
            'harga': summary['harga'],
            'luas': summary['luas'],
            'kota': ', '.join(lokasi_list) or '—'
        }
    else:
        preferensi = {
            'nama': '—',
            'user_text': '—',
            'tipe': ', '.join(tipe_list) or '—',
            'harga': '—',
            'luas': '—',
            'kota': '—'
        }

    # Path gambar tanda tangan (relatif ke static/)
    ttd_path = url_for('static', filename='ttd.png', _external=False)
    print(f"📌 DEBUG: Path TTD = {ttd_path}")

    # Render HTML template
    html = render_template("admin/dashboard_pdf.html",
                           total=total,
                           per_tipe=per_tipe,
                           per_lokasi=per_lokasi,
                           preferensi=preferensi,
                           now=now,
                           ttd_path=ttd_path)

    # Simpan HTML ke file sementara
    with tempfile.NamedTemporaryFile(delete=False, suffix='.html', mode='w', encoding='utf-8') as f:
        f.write(html)
        temp_html_path = f.name

    # Opsi agar wkhtmltopdf bisa akses file lokal (e.g., /static/ttd.png)
    options = {
        'enable-local-file-access': ''
    }

    # Konversi HTML ke PDF
    pdf = pdfkit.from_file(temp_html_path, False,
                           configuration=config, options=options)

    # Kirimkan file PDF sebagai response
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=dashboard.pdf'
    return response
