from flask import Blueprint, render_template
from models.PreferenceModel import get_all_preferences

preferensi_bp = Blueprint('preferensi_bp', __name__)

@preferensi_bp.route('/admin/preferensi')
def daftar_preferensi():
    preferensi_list = get_all_preferences()
    return render_template('admin/preferensi.html', preferensi=preferensi_list)
