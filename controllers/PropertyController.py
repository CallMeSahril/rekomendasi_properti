from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tabulate import tabulate
import re

# Fungsi normalisasi teks harga dari input seperti "1,5 miliar", "800jt", dll
import locale
from datetime import datetime

# Set locale ke Bahasa Indonesia (pastikan OS mendukung)
try:
    locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')  # Linux/Mac
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'ind')  # Windows fallback

now = datetime.now()
formatted_date = now.strftime('%d %B %Y')  # Contoh: 30 Juli 2025


def normalisasi_harga(text):
    text = text.lower().replace(',', '.')
    hasil = []

    pola = re.findall(r'(\d+\.?\d*)\s*(m|miliar|jt|juta|rb|ribu)?', text)

    for jumlah, satuan in pola:
        jumlah = float(jumlah)
        if satuan in ['m', 'miliar']:
            hasil.append(int(jumlah * 1_000_000_000))
        elif satuan in ['jt', 'juta']:
            hasil.append(int(jumlah * 1_000_000))
        elif satuan in ['rb', 'ribu']:
            hasil.append(int(jumlah * 1_000))
        else:
            if 0 < jumlah < 100:
                hasil.append(int(jumlah * 1_000_000_000))  # Anggap miliar
            else:
                hasil.append(int(jumlah * 1_000_000))      # Anggap juta

    return max(hasil) if hasil else None


def process_recommendation(form):
    try:
        nama = form.get('nama', 'Guest')
        user_text = form.get('user_text', '').strip()

        if not user_text:
            return []

        print(f"\n📋 [DEBUG] Nama Pengguna  : {nama}")
        print(f"📋 [DEBUG] Preferensi User: {user_text}")

        from models.PreferenceModel import simpan_preferensi
        from models.AdminModel import get_all_properties, get_tipe_name_by_id

        simpan_preferensi(nama, user_text)
        all_properties = get_all_properties()

        # 🎯 Filter berdasarkan harga maksimal jika terdeteksi
        harga_max = normalisasi_harga(user_text)
        if harga_max:
            print(f"💰 [DEBUG] Harga Maksimal Terdeteksi: Rp{harga_max:,}")
            all_properties = [p for p in all_properties if (
                isinstance(p.get('harga', 0), (int, float)) and p.get('harga', 0) <= harga_max)]
            print(f"📉 [FILTER] Properti tersisa: {len(all_properties)}")
        else:
            print("💰 [DEBUG] Tidak ada harga terdeteksi dari deskripsi pengguna.")

        hasil = []
        tabel_debug = []

        for p in all_properties:
            try:
                harga = p.get('harga', 0)
                if not isinstance(harga, (int, float)):
                    harga = normalisasi_harga(str(harga)) or 0

                deskripsi_awal = str(p.get('deskripsi', '')).strip()
                extra_info = f"{p.get('lokasi', '')} harga {harga} {p.get('tipe', '')} luas tanah {p.get('luas_tanah', '')}m luas bangunan {p.get('luas_bangunan', '')}m kamar {p.get('jumlah_kamar', '')}"
                deskripsi = f"{deskripsi_awal} {extra_info}".lower().strip()

                if not deskripsi:
                    print(
                        f"⚠️ Properti {p.get('nama_properti', 'N/A')} tidak memiliki deskripsi.")
                    continue

                print(f"\n🏠 Properti: {p['nama_properti']}")
                print(f" - Deskripsi Properti: {deskripsi}")

                # TF-IDF dan Cosine Similarity
                vectorizer = TfidfVectorizer()
                vectors = vectorizer.fit_transform(
                    [user_text.lower(), deskripsi]).toarray()
                similarity = cosine_similarity(
                    [vectors[0]], [vectors[1]])[0][0]

                print(f"🔗 Cosine Similarity: {similarity:.4f}")

                hasil.append({
                    'nama': p['nama_properti'],
                    'lokasi': p['lokasi'],
                    'harga': f"Rp{harga:,}",
                    'tipe': get_tipe_name_by_id(p['tipe_id']),
                    'luas_tanah': p.get('luas_tanah', 0),
                    'luas_bangunan': p.get('luas_bangunan', 0),
                    'kamar': p.get('jumlah_kamar', 0),
                    'deskripsi': deskripsi,
                    'similarity': round(similarity, 4),
                    # tambahkan skor_akhir = similarity
                    'skor_akhir': round(similarity, 4),
                })

                tabel_debug.append([
                    p['nama_properti'],
                    f"Rp{harga:,}",
                    get_tipe_name_by_id(p['tipe_id']),
                    p.get('luas_bangunan', 0),
                    p.get('jumlah_kamar', 0),
                    f"{similarity:.4f}"
                ])

            except Exception as e:
                print(
                    f"⚠️ Gagal memproses properti {p.get('nama_properti', 'N/A')}: {e}")
                continue

        if hasil:
            hasil.sort(key=lambda x: x['similarity'], reverse=True)
            print("\n📊 [HASIL REKOMENDASI]")
            print(tabulate(tabel_debug, headers=[
                "Nama", "Harga", "Tipe", "Luas Bangunan", "Kamar", "Similarity"
            ], tablefmt="fancy_grid"))

        return hasil

    except Exception as e:
        import traceback
        print("❌ ERROR Saat proses rekomendasi:")
        print(traceback.format_exc())
        return []
