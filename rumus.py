# from math import radians, sin, cos, sqrt, atan2
# import pandas as pd
# from tabulate import tabulate

# # === 1. PERSIAPAN DAN INTEGRASI DATA ===
# print("1. Persiapan dan Integrasi Data")

# # a. Dataset Properti
# data = [
#     {
#         'nama': 'Rumah Mewah A',
#         'lokasi': 'Jakarta Selatan',
#         'latitude': -6.2607,
#         'longitude': 106.7816,
#         'harga': 1500000000,
#         'tipe': 'Rumah',
#         'luas': 120,
#         'kamar': 3,
#         'deskripsi': 'Rumah mewah dekat pusat kota'
#     },
#     {
#         'nama': 'Apartemen Elite B',
#         'lokasi': 'Jakarta Barat',
#         'latitude': -6.1751,
#         'longitude': 106.8650,
#         'harga': 950000000,
#         'tipe': 'Apartemen',
#         'luas': 60,
#         'kamar': 2,
#         'deskripsi': 'Apartemen modern dengan fasilitas lengkap'
#     },
# ]
# df = pd.DataFrame(data)
# print("a. Dataset Properti:")
# print(tabulate(df, headers="keys", tablefmt="grid"))

# # b. Dataset Kota (Contoh Sederhana)
# df_kota = pd.DataFrame([{
#     'kota': 'Jakarta Selatan',
#     'latitude': -6.2625,
#     'longitude': 106.8203,
# }])
# print("\nb. Dataset Kota:")
# print(tabulate(df_kota, headers="keys", tablefmt="grid"))

# # c. Penggabungan Data & Filter Preferensi
# print("\nc. Penggabungan Data & Filter Preferensi:")
# print("   Tidak dilakukan merge eksplisit, tetapi data akan difilter berdasarkan input pengguna.")

# # === 2. PEMETAAN PROFIL PENGGUNA ===
# user_profile = {
#     'kota': 'Jakarta Selatan',
#     'latitude': -6.2625,
#     'longitude': 106.8203,
#     'harga_min': 900000000,
#     'harga_max': 2000000000,
#     'tipe': 'Rumah',
#     'luas_min': 100,
#     'kamar_min': 2
# }
# print("\n2. Pemetaan Profil Pengguna:")
# print(tabulate([user_profile], headers='keys', tablefmt='grid'))

# print("\n3. Pengolahan Fitur dan Normalisasi")

# # a. One Hot Encoding
# print("   a. One Hot Encoding - Sebelum:")
# print(tabulate(df[['nama', 'tipe']], headers="keys", tablefmt="grid"))

# # Proses Manual: tampilkan langkah one-hot encoding
# print("   🔍 Proses One Hot Encoding:")
# unique_types = df['tipe'].unique()
# print(f"   ➕ Tipe unik yang ditemukan: {list(unique_types)}")

# # Cetak biner untuk setiap baris
# for index, row in df.iterrows():
#     print(f"   - Properti: {row['nama']}")
#     for tipe in unique_types:
#         binary = 1 if row['tipe'] == tipe else 0
#         print(f"     ➤ {tipe}: {'1 (cocok)' if binary == 1 else '0'}")

# # Eksekusi one-hot encoding dengan pandas
# df_encoded = pd.get_dummies(df, columns=['tipe'])

# print("\n   a. One Hot Encoding - Sesudah:")
# print(tabulate(df_encoded, headers="keys", tablefmt="grid"))


# # b. Gabungan Fitur Numerik dan Kategorikal
# features = df[['harga', 'luas', 'kamar']]
# print("\n   b. Gabungan Fitur Numerik dan Kategorikal:")
# print(tabulate(features, headers="keys", tablefmt="grid"))

# # c. Normalisasi Min-Max
# print("\n   c. Normalisasi Min-Max:")

# # Menentukan nilai minimum dan maksimum dari setiap fitur numerik
# min_vals = features.min()
# max_vals = features.max()
# print("     Min Values:")
# print(min_vals.to_string())
# print("     Max Values:")
# print(max_vals.to_string())

# print("\n     🔍 Proses Normalisasi per Baris (Rumus: (x - min) / (max - min)):")
# for i, row in features.iterrows():
#     print(f"     ▪ Properti: {df.loc[i, 'nama']}")
#     for col in features.columns:
#         x = row[col]
#         x_min = min_vals[col]
#         x_max = max_vals[col]
#         normalized = (x - x_min) / (x_max - x_min) if x_max != x_min else 0
#         print(
#             f"       - {col}: ({x} - {x_min}) / ({x_max} - {x_min}) = {normalized:.4f}")
#     print()

# # Lakukan normalisasi
# features_normalized = (features - min_vals) / (max_vals - min_vals)

# print("     ✅ Hasil Normalisasi (Tabel Akhir):")
# print(tabulate(features_normalized, headers="keys", tablefmt="grid"))


# # === 4. PERHITUNGAN KEMIRIPAN ===
# # === 4. PERHITUNGAN KEMIRIPAN ===
# print("\n4. Perhitungan Kemiripan (Menggunakan Rata-rata Fitur Ternormalisasi)")
# print("   Rumus: skor_awal = (harga_norm + luas_norm + kamar_norm) / jumlah_fitur\n")

# # Hitung skor awal sebagai rata-rata dari fitur normalisasi
# scores = features_normalized.mean(axis=1)
# df['skor_awal'] = scores

# # Tampilkan proses per baris
# for i, row in features_normalized.iterrows():
#     nama_properti = df.loc[i, 'nama']
#     harga_norm = row['harga']
#     luas_norm = row['luas']
#     kamar_norm = row['kamar']
#     rata_rata = (harga_norm + luas_norm + kamar_norm) / 3
#     print(f"   ▪ {nama_properti}")
#     print(f"     - harga_norm = {harga_norm:.4f}")
#     print(f"     - luas_norm  = {luas_norm:.4f}")
#     print(f"     - kamar_norm = {kamar_norm:.4f}")
#     print(
#         f"     - skor_awal  = ({harga_norm:.4f} + {luas_norm:.4f} + {kamar_norm:.4f}) / 3 = {rata_rata:.4f}\n")

# # Tampilkan tabel akhir
# print("   ✅ Tabel Skor Awal Kemiripan:")
# print(tabulate(df[['nama', 'skor_awal']], headers='keys', tablefmt='grid'))


# # === 5. PERHITUNGAN JARAK & SKOR AKHIR ===


# def hitung_jarak(lat1, lon1, lat2, lon2):
#     R = 6371  # Radius bumi dalam KM
#     dlat = radians(lat2 - lat1)
#     dlon = radians(lon2 - lon1)
#     a = sin(dlat / 2)**2 + cos(radians(lat1)) * \
#         cos(radians(lat2)) * sin(dlon / 2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))
#     return R * c


# print("\n5. Perhitungan Jarak dan Skor Akhir")

# # a. Perhitungan Jarak
# print("   a. Jarak ke Lokasi Pengguna (Haversine):")
# print("      Rumus Haversine:")
# print("      d = 2 * R * arcsin( sqrt( sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlon/2) ) )\n")

# df['jarak_km'] = df.apply(lambda row: hitung_jarak(
#     user_profile['latitude'], user_profile['longitude'],
#     row['latitude'], row['longitude']
# ), axis=1)

# # Tampilkan perhitungan jarak untuk setiap properti
# for i, row in df.iterrows():
#     nama = row['nama']
#     lat1, lon1 = user_profile['latitude'], user_profile['longitude']
#     lat2, lon2 = row['latitude'], row['longitude']
#     jarak = row['jarak_km']
#     print(f"   ▪ {nama}")
#     print(f"     - Lokasi Pengguna:    ({lat1}, {lon1})")
#     print(f"     - Lokasi Properti:    ({lat2}, {lon2})")
#     print(f"     - Jarak ke Properti:  {jarak:.4f} km\n")

# print("   ✅ Tabel Jarak Properti:")
# print(tabulate(df[['nama', 'jarak_km']], headers='keys', tablefmt='grid'))

# # b. Skor Gabungan
# print("\n   b. Skor Gabungan = Skor Awal / (1 + Jarak KM)")
# df['skor_akhir'] = df['skor_awal'] / (1 + df['jarak_km'])

# # Tampilkan proses perhitungan skor akhir
# for i, row in df.iterrows():
#     nama = row['nama']
#     skor_awal = row['skor_awal']
#     jarak = row['jarak_km']
#     skor_akhir = row['skor_akhir']
#     print(f"   ▪ {nama}")
#     print(f"     - skor_awal = {skor_awal:.4f}")
#     print(f"     - jarak_km  = {jarak:.4f}")
#     print(
#         f"     - skor_akhir = {skor_awal:.4f} / (1 + {jarak:.4f}) = {skor_akhir:.4f}\n")

# print("   ✅ Tabel Skor Gabungan:")
# print(tabulate(df[['nama', 'skor_awal', 'jarak_km',
#       'skor_akhir']], headers='keys', tablefmt='grid'))

# # c. Peringkat Akhir
# df_sorted = df.sort_values(
#     by='skor_akhir', ascending=False).reset_index(drop=True)
# df_sorted['peringkat'] = df_sorted.index + 1

# print("   c. Peringkat Properti Berdasarkan Skor Akhir:")
# print(tabulate(df_sorted[['peringkat', 'nama',
#       'skor_akhir']], headers='keys', tablefmt='grid'))
import pandas as pd
from math import radians, sin, cos, sqrt, atan2
from tabulate import tabulate

# ===== 1. Dataset Properti =====
data = [
    {
        'nama': 'Rumah Mewah A',
        'lokasi': 'Jakarta Selatan',
        'latitude': -6.2607,
        'longitude': 106.7816,
        'harga': 1500000000,
        'tipe': 'Rumah',
        'luas': 120,
        'kamar': 3,
        'deskripsi': 'Rumah mewah dekat pusat kota'
    },
    {
        'nama': 'Apartemen Elite B',
        'lokasi': 'Jakarta Barat',
        'latitude': -6.1751,
        'longitude': 106.8650,
        'harga': 950000000,
        'tipe': 'Apartemen',
        'luas': 60,
        'kamar': 2,
        'deskripsi': 'Apartemen modern dengan fasilitas lengkap'
    },
    {
        'nama': 'Rumah Minimalis C',
        'lokasi': 'Jakarta Selatan',
        'latitude': -6.2650,
        'longitude': 106.8300,
        'harga': 1200000000,
        'tipe': 'Rumah',
        'luas': 90,
        'kamar': 2,
        'deskripsi': 'Rumah minimalis terjangkau'
    },
    {
        'nama': 'Rumah Taman Hijau D',
        'lokasi': 'Jakarta Timur',
        'latitude': -6.2250,
        'longitude': 106.9000,
        'harga': 1100000000,
        'tipe': 'Rumah',
        'luas': 100,
        'kamar': 3,
        'deskripsi': 'Rumah asri dekat taman dan sekolah'
    },
    {
        'nama': 'Apartemen SkyView E',
        'lokasi': 'Jakarta Pusat',
        'latitude': -6.1810,
        'longitude': 106.8380,
        'harga': 1300000000,
        'tipe': 'Apartemen',
        'luas': 85,
        'kamar': 2,
        'deskripsi': 'Pemandangan kota dari lantai atas'
    },
    #     {
    #         'nama': 'Rumah Klasik F',
    #         'lokasi': 'Jakarta Selatan',
    #         'latitude': -6.2700,
    #         'longitude': 106.8000,
    #         'harga': 1000000000,
    #         'tipe': 'Rumah',
    #         'luas': 110,
    #         'kamar': 2,
    #         'deskripsi': 'Rumah gaya klasik dengan halaman luas'
    #     },
    #     {
    #         'nama': 'Apartemen Budget G',
    #         'lokasi': 'Jakarta Timur',
    #         'latitude': -6.2200,
    #         'longitude': 106.9100,
    #         'harga': 850000000,
    #         'tipe': 'Apartemen',
    #         'luas': 45,
    #         'kamar': 1,
    #         'deskripsi': 'Cocok untuk mahasiswa dan profesional muda'
    #     },
    #     {
    #         'nama': 'Rumah Elite Cluster H',
    #         'lokasi': 'Jakarta Selatan',
    #         'latitude': -6.2550,
    #         'longitude': 106.7900,
    #         'harga': 1700000000,
    #         'tipe': 'Rumah',
    #         'luas': 150,
    #         'kamar': 4,
    #         'deskripsi': 'Rumah cluster elit dengan keamanan 24 jam'
    #     },
    #     {
    #         'nama': 'Apartemen Cozy I',
    #         'lokasi': 'Jakarta Barat',
    #         'latitude': -6.1800,
    #         'longitude': 106.8500,
    #         'harga': 1050000000,
    #         'tipe': 'Apartemen',
    #         'luas': 70,
    #         'kamar': 2,
    #         'deskripsi': 'Apartemen nyaman dengan akses mall langsung'
    #     },
    #     {
    #         'nama': 'Rumah Pinggiran J',
    #         'lokasi': 'Jakarta Utara',
    #         'latitude': -6.1300,
    #         'longitude': 106.8800,
    #         'harga': 950000000,
    #         'tipe': 'Rumah',
    #         'luas': 95,
    #         'kamar': 2,
    #         'deskripsi': 'Rumah sederhana di pinggiran kota'
    #     }
    # ]
]
# data += [
#     {
#         'nama': 'Rumah Modern K',
#         'lokasi': 'Jakarta Timur',
#         'latitude': -6.2400,
#         'longitude': 106.9100,
#         'harga': 1250000000,
#         'tipe': 'Rumah',
#         'luas': 105,
#         'kamar': 3,
#         'deskripsi': 'Rumah modern dengan konsep terbuka'
#     },
#     {
#         'nama': 'Apartemen Strategis L',
#         'lokasi': 'Jakarta Selatan',
#         'latitude': -6.2580,
#         'longitude': 106.7990,
#         'harga': 1150000000,
#         'tipe': 'Apartemen',
#         'luas': 75,
#         'kamar': 2,
#         'deskripsi': 'Dekat stasiun MRT dan perkantoran'
#     },
#     {
#         'nama': 'Rumah Keluarga M',
#         'lokasi': 'Jakarta Barat',
#         'latitude': -6.1805,
#         'longitude': 106.8655,
#         'harga': 980000000,
#         'tipe': 'Rumah',
#         'luas': 100,
#         'kamar': 3,
#         'deskripsi': 'Ideal untuk keluarga dengan anak-anak'
#     },
#     {
#         'nama': 'Rumah Minimalis N',
#         'lokasi': 'Jakarta Utara',
#         'latitude': -6.1400,
#         'longitude': 106.8900,
#         'harga': 880000000,
#         'tipe': 'Rumah',
#         'luas': 85,
#         'kamar': 2,
#         'deskripsi': 'Rumah minimalis, cocok untuk pasangan muda'
#     },
#     {
#         'nama': 'Apartemen View Danau O',
#         'lokasi': 'Jakarta Barat',
#         'latitude': -6.1700,
#         'longitude': 106.8600,
#         'harga': 1020000000,
#         'tipe': 'Apartemen',
#         'luas': 78,
#         'kamar': 2,
#         'deskripsi': 'Apartemen dengan pemandangan danau'
#     },
#     {
#         'nama': 'Rumah Asri P',
#         'lokasi': 'Jakarta Timur',
#         'latitude': -6.2300,
#         'longitude': 106.9050,
#         'harga': 990000000,
#         'tipe': 'Rumah',
#         'luas': 98,
#         'kamar': 2,
#         'deskripsi': 'Rumah tenang dengan taman pribadi'
#     },
#     {
#         'nama': 'Apartemen Premium Q',
#         'lokasi': 'Jakarta Pusat',
#         'latitude': -6.1820,
#         'longitude': 106.8350,
#         'harga': 1600000000,
#         'tipe': 'Apartemen',
#         'luas': 100,
#         'kamar': 3,
#         'deskripsi': 'Fasilitas lengkap, cocok untuk eksekutif'
#     },
#     {
#         'nama': 'Rumah Tropis R',
#         'lokasi': 'Jakarta Selatan',
#         'latitude': -6.2500,
#         'longitude': 106.7900,
#         'harga': 1400000000,
#         'tipe': 'Rumah',
#         'luas': 115,
#         'kamar': 3,
#         'deskripsi': 'Rumah tropis dengan sirkulasi udara alami'
#     },
#     {
#         'nama': 'Apartemen Studio S',
#         'lokasi': 'Jakarta Timur',
#         'latitude': -6.2350,
#         'longitude': 106.9200,
#         'harga': 780000000,
#         'tipe': 'Apartemen',
#         'luas': 35,
#         'kamar': 1,
#         'deskripsi': 'Studio apartemen hemat untuk profesional muda'
#     },
#     {
#         'nama': 'Rumah Sederhana T',
#         'lokasi': 'Jakarta Utara',
#         'latitude': -6.1250,
#         'longitude': 106.8900,
#         'harga': 920000000,
#         'tipe': 'Rumah',
#         'luas': 90,
#         'kamar': 2,
#         'deskripsi': 'Rumah sederhana dengan akses jalan utama'
#     }
# ]
# data += [
#     {
#         'nama': 'Rumah Lantai 2 U',
#         'lokasi': 'Jakarta Timur',
#         'latitude': -6.2450,
#         'longitude': 106.9120,
#         'harga': 1350000000,
#         'tipe': 'Rumah',
#         'luas': 130,
#         'kamar': 4,
#         'deskripsi': 'Rumah 2 lantai luas dan nyaman untuk keluarga besar'
#     },
#     {
#         'nama': 'Apartemen CityLink V',
#         'lokasi': 'Jakarta Pusat',
#         'latitude': -6.1808,
#         'longitude': 106.8305,
#         'harga': 1080000000,
#         'tipe': 'Apartemen',
#         'luas': 72,
#         'kamar': 2,
#         'deskripsi': 'Apartemen dengan koneksi langsung ke pusat perbelanjaan'
#     },
#     {
#         'nama': 'Rumah Cluster W',
#         'lokasi': 'Jakarta Selatan',
#         'latitude': -6.2535,
#         'longitude': 106.7820,
#         'harga': 1450000000,
#         'tipe': 'Rumah',
#         'luas': 125,
#         'kamar': 3,
#         'deskripsi': 'Rumah cluster aman dan nyaman'
#     },
#     {
#         'nama': 'Apartemen Mewah X',
#         'lokasi': 'Jakarta Barat',
#         'latitude': -6.1705,
#         'longitude': 106.8500,
#         'harga': 1550000000,
#         'tipe': 'Apartemen',
#         'luas': 95,
#         'kamar': 3,
#         'deskripsi': 'Apartemen high-end dengan pemandangan kota'
#     },
#     {
#         'nama': 'Rumah Samping Sekolah Y',
#         'lokasi': 'Jakarta Utara',
#         'latitude': -6.1350,
#         'longitude': 106.8805,
#         'harga': 970000000,
#         'tipe': 'Rumah',
#         'luas': 88,
#         'kamar': 2,
#         'deskripsi': 'Dekat sekolah dan cocok untuk keluarga kecil'
#     },
#     {
#         'nama': 'Rumah Industrial Z',
#         'lokasi': 'Jakarta Selatan',
#         'latitude': -6.2680,
#         'longitude': 106.8050,
#         'harga': 1380000000,
#         'tipe': 'Rumah',
#         'luas': 118,
#         'kamar': 3,
#         'deskripsi': 'Desain modern industrial yang unik'
#     },
#     {
#         'nama': 'Apartemen Transit AA',
#         'lokasi': 'Jakarta Timur',
#         'latitude': -6.2210,
#         'longitude': 106.9300,
#         'harga': 820000000,
#         'tipe': 'Apartemen',
#         'luas': 40,
#         'kamar': 1,
#         'deskripsi': 'Akses cepat ke transportasi umum dan tol'
#     },
#     {
#         'nama': 'Rumah Dekat Bandara AB',
#         'lokasi': 'Jakarta Barat',
#         'latitude': -6.1708,
#         'longitude': 106.7900,
#         'harga': 1250000000,
#         'tipe': 'Rumah',
#         'luas': 105,
#         'kamar': 3,
#         'deskripsi': 'Strategis untuk pekerja yang sering bepergian'
#     },
#     {
#         'nama': 'Apartemen Compact AC',
#         'lokasi': 'Jakarta Pusat',
#         'latitude': -6.1850,
#         'longitude': 106.8400,
#         'harga': 750000000,
#         'tipe': 'Apartemen',
#         'luas': 38,
#         'kamar': 1,
#         'deskripsi': 'Unit kecil untuk lajang atau pasangan muda'
#     },
#     {
#         'nama': 'Rumah Vintage AD',
#         'lokasi': 'Jakarta Selatan',
#         'latitude': -6.2610,
#         'longitude': 106.7750,
#         'harga': 1190000000,
#         'tipe': 'Rumah',
#         'luas': 102,
#         'kamar': 3,
#         'deskripsi': 'Rumah dengan gaya arsitektur vintage klasik'
#     }
# ]

df = pd.DataFrame(data)
# Cetak tabel menggunakan tabulate
print("=== Dataset Properti ===")
print(tabulate(df, headers='keys', tablefmt='pretty'))
# ===== 2. Profil Preferensi Pengguna =====
user_profile = {
    'kota': 'Jakarta Selatan',
    'latitude': -6.2625,
    'longitude': 106.8203,
    'harga_min': 900000000,
    'harga_max': 2000000000,
    'tipe': 'Rumah',
    'luas_min': 100,
    'kamar_min': 2
}
# ===== Tampilkan Profil Preferensi Pengguna =====
user_df = pd.DataFrame([user_profile])  # Konversi dictionary ke DataFrame
print("\n=== Profil Preferensi Pengguna ===")
print(tabulate(user_df, headers='keys', tablefmt='pretty'))

# ===== 3. Filter Properti Berdasarkan Preferensi Pengguna =====
filtered_df = df[
    (df['harga'] >= user_profile['harga_min']) &
    (df['harga'] <= user_profile['harga_max']) &
    (df['tipe'] == user_profile['tipe']) &
    (df['luas'] >= user_profile['luas_min']) &
    (df['kamar'] >= user_profile['kamar_min'])
].copy()
print("=== 3. Penyaringan Properti ===")
print("Preferensi pengguna:")
print(f" - Kota: {user_profile['kota']}")
print(
    f" - Harga: Rp{user_profile['harga_min']} - Rp{user_profile['harga_max']}")
print(f" - Tipe: {user_profile['tipe']}")
print(f" - Luas minimal: {user_profile['luas_min']} m²")
print(f" - Kamar minimal: {user_profile['kamar_min']}\n")

# a. Filter harga minimal
filter_harga_min = df['harga'] >= user_profile['harga_min']
print("a. Filter harga minimal:")
print(
    f"  Kondisi: df['harga'] >= user_profile['harga_min'] → {user_profile['harga_min']}")
print("  Artinya: Harga properti harus lebih besar atau sama dengan batas minimal preferensi pengguna\n")

# Tampilkan hasil evaluasi per baris
for i in range(len(df)):
    nama = df.loc[i, 'nama']
    harga = df.loc[i, 'harga']
    batas_min = user_profile['harga_min']
    hasil = filter_harga_min.iloc[i]
    print(f"  {i}. {nama} | Harga: Rp{harga:,} ≥ Rp{batas_min:,} → {'✅ Lolos' if hasil else '❌ Tidak Lolos'}")

print()
# b. Filter harga maksimal
filter_harga_max = df['harga'] <= user_profile['harga_max']
print("b. Filter harga maksimal:")
print(
    f"  Kondisi: df['harga'] <= user_profile['harga_max'] → {user_profile['harga_max']}")
print("  Artinya: Harga properti harus lebih kecil atau sama dengan batas maksimal preferensi pengguna\n")

for i in range(len(df)):
    nama = df.loc[i, 'nama']
    harga = df.loc[i, 'harga']
    batas_max = user_profile['harga_max']
    hasil = filter_harga_max.iloc[i]
    print(f"  {i}. {nama} | Harga: Rp{harga:,} ≤ Rp{batas_max:,} → {'✅ Lolos' if hasil else '❌ Tidak Lolos'}")

print()


# c. Filter tipe properti
filter_tipe = df['tipe'] == user_profile['tipe']
print("c. Filter tipe properti:")
print(
    f"  Kondisi: df['tipe'] == user_profile['tipe'] → '{user_profile['tipe']}'")
print("  Artinya: Tipe properti harus sama persis dengan tipe pilihan pengguna\n")

for i in range(len(df)):
    nama = df.loc[i, 'nama']
    tipe = df.loc[i, 'tipe']
    pilihan = user_profile['tipe']
    hasil = filter_tipe.iloc[i]
    print(f"  {i}. {nama} | Tipe: {tipe} == {pilihan} → {'✅ Sesuai' if hasil else '❌ Tidak Sesuai'}")

print()


# d. Filter luas minimal
filter_luas = df['luas'] >= user_profile['luas_min']
print("d. Filter luas minimal:")
print(
    f"  Kondisi: df['luas'] >= user_profile['luas_min'] → {user_profile['luas_min']} m²")
print("  Artinya: Luas bangunan harus lebih besar atau sama dengan luas minimal yang diminta pengguna\n")

for i in range(len(df)):
    nama = df.loc[i, 'nama']
    luas = df.loc[i, 'luas']
    luas_min = user_profile['luas_min']
    hasil = filter_luas.iloc[i]
    print(f"  {i}. {nama} | Luas: {luas} m² ≥ {luas_min} m² → {'✅ Sesuai' if hasil else '❌ Tidak Sesuai'}")

print()


# e. Filter jumlah kamar minimal
filter_kamar = df['kamar'] >= user_profile['kamar_min']
print("e. Filter jumlah kamar minimal:")
print(
    f"  Kondisi: df['kamar'] >= user_profile['kamar_min'] → {user_profile['kamar_min']}")
print("  Artinya: Jumlah kamar harus lebih besar atau sama dengan jumlah minimal kamar yang dibutuhkan pengguna\n")

for i in range(len(df)):
    nama = df.loc[i, 'nama']
    kamar = df.loc[i, 'kamar']
    kamar_min = user_profile['kamar_min']
    hasil = filter_kamar.iloc[i]
    print(f"  {i}. {nama} | Kamar: {kamar} ≥ {kamar_min} → {'✅ Sesuai' if hasil else '❌ Tidak Sesuai'}")

print()


# f. Gabungkan semua filter
combined_filter = filter_harga_min & filter_harga_max & filter_tipe & filter_luas & filter_kamar
print("f. Gabungan semua filter:")
print("  Semua kondisi (a–e) harus terpenuhi (True) agar properti lolos seleksi akhir\n")

for i in range(len(df)):
    nama = df.loc[i, 'nama']
    hasil = combined_filter.iloc[i]
    print(f"  {i}. {nama} → {'✅ Lolos Semua Filter' if hasil else '❌ Gagal'}")
tabel_gabungan = df[['nama']].copy()
tabel_gabungan['Lolos Semua Filter'] = combined_filter.values

tabel_gabungan = df[['nama']].copy()
tabel_gabungan['Harga Min'] = filter_harga_min.values
tabel_gabungan['Harga Max'] = filter_harga_max.values
tabel_gabungan['Tipe'] = filter_tipe.values
tabel_gabungan['Luas'] = filter_luas.values
tabel_gabungan['Kamar'] = filter_kamar.values
tabel_gabungan['Lolos Semua'] = combined_filter.values

print("📋 Tabel Detail Gabungan Filter:")
print(tabel_gabungan.to_string(index=True))


# g. Tampilkan properti yang lolos filter
filtered_df = df[combined_filter].copy()
print("g. ✅ Daftar Listing yang Lolos Semua Filter:\n")

if filtered_df.empty:
    print("  ⚠️ Tidak ada properti yang memenuhi semua kriteria.")
else:
    for i, row in filtered_df.iterrows():
        print(f"  {i}. {row['nama']}")
        print(f"     Lokasi : {row['lokasi']}")
        print(f"     Harga  : Rp{row['harga']:,}")
        print(f"     Tipe   : {row['tipe']}")
        print(f"     Luas   : {row['luas']} m²")
        print(f"     Kamar  : {row['kamar']}\n")

print("📋 Tabel Properti yang Lolos Semua Filter:")
if filtered_df.empty:
    print("  ⚠️ Tidak ada properti yang memenuhi semua kriteria.")
else:
    tabel = filtered_df[['nama', 'lokasi', 'harga', 'tipe', 'luas', 'kamar']]
    print(tabulate(tabel, headers='keys', tablefmt='fancy_grid', showindex=True))

# Jika tidak ada properti cocok, return kosong
if filtered_df.empty:
    print("Tidak ada properti yang sesuai preferensi pengguna.")
else:
    print("\n=== Properti yang Sesuai Preferensi Pengguna ===")
    print(tabulate(filtered_df, headers='keys', tablefmt='pretty'))
    # ===== 4. One-Hot Encoding untuk Fitur Kategorikal =====
    print("=== Proses One-Hot Encoding Kolom 'tipe' ===\n")
    # Tampilkan tabel sebelum One-Hot Encoding
    print("\n=== Tabel Sebelum One-Hot Encoding ===")
    print(tabulate(filtered_df[['nama', 'lokasi', 'harga', 'tipe',
          'luas', 'kamar']], headers='keys', tablefmt='pretty'))
    print("\n=== Proses One-Hot Encoding Kolom 'tipe' ===\n")

    # Dapatkan kategori unik dari kolom 'tipe'
    unique_tipes = filtered_df['tipe'].unique().tolist()
    print(f"Kategori unik dari kolom 'tipe': {unique_tipes}\n")

    # Tampilkan penjelasan representasi One-Hot untuk tiap properti
    for i, row in filtered_df.iterrows():
        tipe_asli = row['tipe']
        print(f"{i}. Properti: {row['nama']}")
        print(f"   Tipe Asli  : {tipe_asli}")
        print(f"   Representasi One-Hot:")
        for tipe in unique_tipes:
            nilai = 1 if tipe_asli == tipe else 0
            simbol = "✅" if nilai == 1 else "❌"
            print(
                f"     tipe_{tipe:<10}: {nilai} {simbol} ({'1 jika cocok' if nilai == 1 else '0 jika tidak cocok'})")
        print()

    # Lakukan One-Hot Encoding
    filtered_df = pd.get_dummies(filtered_df, columns=['tipe'])

    # Tampilkan hasil setelah One-Hot Encoding
    print("\n=== Tabel Setelah One-Hot Encoding ===")
    print(tabulate(filtered_df, headers='keys', tablefmt='pretty'))

    # # ===== 5. Normalisasi Min-Max untuk Fitur Numerik =====
    # fitur_numerik = filtered_df[['harga', 'luas', 'kamar']]

    # # Simpan nilai min dan max untuk ditampilkan
    # min_values = fitur_numerik.min()
    # max_values = fitur_numerik.max()

    # # Lakukan normalisasi
    # # Cegah pembagian 0 (normalisasi aman)
    # fitur_normalized = fitur_numerik.copy()
    # for col in fitur_numerik.columns:
    #     col_min = min_values[col]
    #     col_max = max_values[col]
    #     if col_max - col_min == 0:
    #         fitur_normalized[col] = 0.0  # Atur default normalisasi jadi 0
    #     else:
    #         fitur_normalized[col] = (
    #             fitur_numerik[col] - col_min) / (col_max - col_min)

    # filtered_df[['harga_norm', 'luas_norm', 'kamar_norm']] = fitur_normalized

    # # Gabungkan hasil ke satu DataFrame untuk ditampilkan
    # normalisasi_df = filtered_df[[
    #     'nama', 'harga', 'luas', 'kamar', 'harga_norm', 'luas_norm', 'kamar_norm']]

    # # Tampilkan tabel hasil normalisasi
    # from tabulate import tabulate
    # print("\n=== Hasil Normalisasi Min-Max (harga, luas, kamar) ===")
    # print(tabulate(normalisasi_df, headers='keys', tablefmt='pretty'))

    # # Tampilkan nilai min dan max untuk referensi
    # print("\n=== Nilai Minimum dan Maksimum Setiap Fitur ===")
    # for col in ['harga', 'luas', 'kamar']:
    #     print(f"- {col}: min = {min_values[col]}, max = {max_values[col]}")
    # ===== 5. Normalisasi Min-Max untuk Fitur Numerik =====
    # Ambil kolom numerik
    fitur_numerik = filtered_df[['harga', 'luas', 'kamar']]

    # Simpan nilai min dan max untuk ditampilkan
    min_values = fitur_numerik.min()
    max_values = fitur_numerik.max()

    # Lakukan normalisasi
    fitur_normalized = fitur_numerik.copy()

    # Reset index agar aman digunakan dalam perulangan
    filtered_df = filtered_df.reset_index(drop=True)

    # Perhitungan normalisasi + tampilkan proses matematis
    print("\n=== Proses Normalisasi Min-Max ===")
    for i in range(len(filtered_df)):
        nama = filtered_df.loc[i, 'nama']
        print(f"\nProperti: {nama}")

        for col in ['harga', 'luas', 'kamar']:
            val = filtered_df.loc[i, col]
            min_val = min_values[col]
            max_val = max_values[col]

            if max_val - min_val == 0:
                norm = 0.0
            else:
                norm = (val - min_val) / (max_val - min_val)

            fitur_normalized.loc[i, col] = norm
            print(
                f"  {col.capitalize()}:\n    Normalisasi: ({val} - {min_val}) / ({max_val} - {min_val}) = {norm:.4f}")

    # Masukkan kolom hasil normalisasi ke DataFrame utama
    filtered_df[['harga_norm', 'luas_norm', 'kamar_norm']] = fitur_normalized

    # Gabungkan hasil untuk ditampilkan
    normalisasi_df = filtered_df[[
        'nama', 'harga', 'luas', 'kamar', 'harga_norm', 'luas_norm', 'kamar_norm'
    ]]

    # Tampilkan tabel hasil normalisasi
    from tabulate import tabulate
    print("\n=== Tabel Hasil Normalisasi Min-Max (harga, luas, kamar) ===")
    print(tabulate(normalisasi_df, headers='keys', tablefmt='pretty'))

    # Tampilkan nilai min dan max untuk referensi
    print("\n=== Nilai Minimum dan Maksimum Setiap Fitur ===")
    for col in ['harga', 'luas', 'kamar']:
        print(f"- {col}: min = {min_values[col]}, max = {max_values[col]}")

    # ===== 6. Hitung Skor Kemiripan Berdasarkan Fitur =====
    filtered_df['skor_awal'] = fitur_normalized.mean(axis=1)
    # ===== Tampilkan Skor Awal =====
    skor_df = filtered_df[['nama', 'harga_norm',
                           'luas_norm', 'kamar_norm', 'skor_awal']]

    print("\n=== Skor Kemiripan Awal Berdasarkan Fitur (Rata-Rata Normalisasi) ===")
    print(tabulate(skor_df, headers='keys', tablefmt='pretty'))
    for i in range(len(filtered_df)):
        nama = filtered_df.loc[i, 'nama']
        harga_n = filtered_df.loc[i, 'harga_norm']
        luas_n = filtered_df.loc[i, 'luas_norm']
        kamar_n = filtered_df.loc[i, 'kamar_norm']
        skor = filtered_df.loc[i, 'skor_awal']

        print(f"\nProperti: {nama}")
        print(f"  Skor Awal = (harga_norm + luas_norm + kamar_norm) / 3")
        print(
            f"            = ({harga_n:.4f} + {luas_n:.4f} + {kamar_n:.4f}) / 3 = {skor:.4f}")

    # # ===== 7. Hitung Jarak Lokasi ke Pengguna (Haversine) =====
    # ===== Cetak Proses Perhitungan Haversine Jarak Properti ke Lokasi Pengguna =====
    print("\n=== Proses Perhitungan Jarak Lokasi (Haversine) ===")

    def haversine(lat1, lon1, lat2, lon2):
        R = 6371  # km
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * \
            cos(radians(lat2)) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c

    for idx, row in filtered_df.iterrows():
        lat1, lon1 = user_profile['latitude'], user_profile['longitude']
        lat2, lon2 = row['latitude'], row['longitude']

        # Konversi ke radian
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        rlat1 = radians(lat1)
        rlat2 = radians(lat2)

        # Perhitungan rumus
        a = sin(dlat / 2) ** 2 + cos(rlat1) * cos(rlat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        R = 6371  # Radius bumi
        jarak = R * c

        print(f"\nProperti: {row['nama']}")
        print(f"→ Δlat (rad): {dlat:.6f}")
        print(f"→ Δlon (rad): {dlon:.6f}")
        print(f"→ a: {a:.6f}")
        print(f"→ c: {c:.6f}")
        print(f"→ Jarak (km): {jarak:.2f}")

        filtered_df['jarak_km'] = filtered_df.apply(
            lambda row: haversine(
                user_profile['latitude'], user_profile['longitude'], row['latitude'], row['longitude']),
            axis=1
        )
        for idx, row in filtered_df.iterrows():
            nama_properti = row['nama']
            lat1, lon1 = user_profile['latitude'], user_profile['longitude']
            lat2, lon2 = row['latitude'], row['longitude']

            print(f"\n📍 Properti: {nama_properti}")
            print(f"Koordinat Pengguna  : lat1 = {lat1}, lon1 = {lon1}")
            print(f"Koordinat Properti  : lat2 = {lat2}, lon2 = {lon2}")

            # Rumus
            print("\n🔢 Langkah Perhitungan Haversine:")
            print("1. Konversi ke radian:")
            print(
                f"   dlat = radians({lat2} - {lat1}) = {radians(lat2 - lat1):.6f}")
            print(
                f"   dlon = radians({lon2} - {lon1}) = {radians(lon2 - lon1):.6f}")
            print(f"   rlat1 = radians({lat1}) = {radians(lat1):.6f}")
            print(f"   rlat2 = radians({lat2}) = {radians(lat2):.6f}")

            dlat = radians(lat2 - lat1)
            dlon = radians(lon2 - lon1)
            rlat1 = radians(lat1)
            rlat2 = radians(lat2)

            a = sin(dlat / 2) ** 2 + cos(rlat1) * \
                cos(rlat2) * sin(dlon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            jarak = 6371 * c

            print("2. Hitung a:")
            print(f"   a = sin²(dlat/2) + cos(rlat1) * cos(rlat2) * sin²(dlon/2)")
            print(
                f"     = {sin(dlat / 2) ** 2:.6f} + {cos(rlat1):.6f} * {cos(rlat2):.6f} * {sin(dlon / 2) ** 2:.6f}")
            print(f"     = {a:.6f}")

            print("3. Hitung c:")
            print(f"   c = 2 * atan2(√a, √(1 - a)) = {c:.6f}")

            print("4. Hitung jarak:")
            print(f"   jarak = R * c = 6371 * {c:.6f} = {jarak:.2f} km")

    # ===== 8. Perhitungan Skor Akhir dengan Penalti Berdasarkan Jarak =====
    filtered_df['skor_akhir'] = filtered_df['skor_awal'] / \
        (1 + filtered_df['jarak_km'])

    # Tampilkan proses perhitungan skor akhir
    print("\n=== Perhitungan Skor Akhir (Dengan Penalti Jarak) ===")

    for idx, row in filtered_df.iterrows():
        nama_properti = row['nama']
        skor_awal = row['skor_awal']
        jarak = row['jarak_km']
        skor_akhir = row['skor_akhir']

        print(f"\nProperti : {nama_properti}")
        print(f"→ Skor Awal      : {skor_awal:.4f}")
        print(f"→ Jarak ke User  : {jarak:.2f} km")
        print(f"→ Skor Akhir     = {skor_awal:.4f} / (1 + {jarak:.2f})")
        print(f"→ Skor Akhir     = {skor_akhir:.4f}")

    # ===== 9. Urutkan Berdasarkan Skor Akhir =====
    hasil_rekomendasi = filtered_df.sort_values(
        by='skor_akhir', ascending=False).reset_index(drop=True)
    hasil_rekomendasi['peringkat'] = hasil_rekomendasi.index + 1

    # Tampilkan hasil urutan dan peringkat
    tabel_peringkat = hasil_rekomendasi[[
        'peringkat', 'nama', 'skor_awal', 'jarak_km', 'skor_akhir'
    ]]

    from tabulate import tabulate
    print("\n=== Hasil Rekomendasi Properti Berdasarkan Skor Akhir ===")
    print(tabulate(tabel_peringkat, headers='keys',
          tablefmt='pretty', floatfmt=".4f"))

    # ===== 10. Tampilkan Hasil Rekomendasi =====
    kolom_output = ['peringkat', 'nama', 'lokasi',
                    'harga', 'luas', 'kamar', 'skor_akhir']
    print(hasil_rekomendasi[kolom_output])
