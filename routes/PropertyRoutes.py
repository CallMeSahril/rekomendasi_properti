from flask import Blueprint, render_template, request
from controllers.PropertyController import process_recommendation
from models.PropertyModel import fetch_all_cities
from models.AdminModel import get_all_property_types

property_bp = Blueprint('property_bp', __name__)


@property_bp.route('/')
def index():
    kota_list = fetch_all_cities()
    tipe_list = get_all_property_types()  # ganti dari get_properties_by_type()
    return render_template('index.html', kota_list=kota_list, tipe_list=tipe_list)


@property_bp.route('/rekomendasi', methods=['POST'])
def rekomendasi():
    hasil = process_recommendation(request.form)

    # Validasi hasil harus list
    if not isinstance(hasil, list):
        hasil = []

    print(f"\n📋 Rekomendasi: {len(hasil)} properti ditemukan.")

    # Konversi harga ke integer untuk setiap properti
    for p in hasil:
        try:
            harga_text = str(p.get('harga', '')).replace(
                '.', '').replace(',', '')
            p['harga'] = int(''.join(filter(str.isdigit, harga_text)))
        except:
            p['harga'] = 0
        print(p)

    print(f"📋 Rekomendasi: {len(hasil)} properti dengan harga terkonversi.")
    return render_template('hasil.html', hasil=hasil)
