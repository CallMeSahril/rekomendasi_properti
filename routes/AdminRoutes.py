from flask import Blueprint
from controllers import AdminController

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin/properti')

admin_bp.route('/', methods=['GET'])(AdminController.list_properti)
# ✅ Tambahkan ini
admin_bp.route('/dashboard', methods=['GET'])(AdminController.dashboard)
admin_bp.route('/tambah', methods=['GET']
               )(AdminController.form_tambah_properti)
admin_bp.route('/tambah', methods=['POST'])(AdminController.tambah_properti)
admin_bp.route('/edit/<int:id>',
               methods=['GET'])(AdminController.form_edit_properti)
admin_bp.route('/edit/<int:id>',
               methods=['POST'])(AdminController.update_properti)
admin_bp.route('/hapus/<int:id>',
               methods=['GET'])(AdminController.hapus_properti)
admin_bp.route('/laporan/properti/cetak',
               methods=['GET'])(AdminController.cetak_laporan_properti)
