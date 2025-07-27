from flask import Blueprint, render_template, request, redirect, session, url_for, flash

auth_bp = Blueprint('auth_bp', __name__)

# Dummy akun admin
ADMIN_CREDENTIAL = {
    'email': 'admin@gmail.com',
    'password': 'tes123'
}


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == ADMIN_CREDENTIAL['email'] and password == ADMIN_CREDENTIAL['password']:
            session['admin_logged_in'] = True
            # ⬅️ redirect ke dashboard
            return redirect(url_for('admin_bp.dashboard'))
        else:
            flash('Email atau password salah!', 'error')
            return redirect(url_for('auth_bp.login'))

    return render_template('admin/login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Berhasil logout.", "success")
    # ⬅️ redirect ke halaman utama properti
    return redirect(url_for('property_bp.index'))
