from flask import Blueprint
from controllers import LaporanController

laporan_bp = Blueprint("laporan_bp", __name__, url_prefix="/admin")

laporan_bp.route("/laporan", endpoint="laporan")(LaporanController.laporan_menu)
laporan_bp.route("/laporan/properti", endpoint="laporan_properti")(LaporanController.laporan_properti)
laporan_bp.route("/laporan/preferensi", endpoint="laporan_preferensi")(LaporanController.laporan_preferensi)
laporan_bp.route("/laporan/statistik", endpoint="laporan_statistik")(LaporanController.laporan_statistik)
laporan_bp.route("/laporan/rekomendasi", endpoint="laporan_rekomendasi")(LaporanController.laporan_rekomendasi)
