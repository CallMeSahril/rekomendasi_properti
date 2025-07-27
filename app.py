from flask import Flask
from models.PropertyModel import init_mysql
from routes.PropertyRoutes import property_bp
from routes.AdminRoutes import admin_bp
from routes.DashboardRoutes import dashboard_bp
from routes.PenjelasanRoutes import penjelasan_bp
from routes.AuthRoutes import auth_bp
from routes.PreferensiRoutes import preferensi_bp
from routes.LaporanRoute import laporan_bp
app = Flask(__name__)
app.secret_key = 'my_super_secret_key_123456'

init_mysql(app)
app.register_blueprint(property_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(penjelasan_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(preferensi_bp)
app.register_blueprint(laporan_bp)

if __name__ == '__main__':
    app.run(port="5021", host="0.0.0.0", debug=True)
