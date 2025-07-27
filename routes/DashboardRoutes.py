from flask import Blueprint
from controllers import DashboardController

dashboard_bp = Blueprint("dashboard_bp", __name__, url_prefix="/admin")

dashboard_bp.route("/dashboard")(DashboardController.dashboard)
dashboard_bp.route("/dashboard/cetak",
                   methods=["GET"])(DashboardController.dashboard_pdf)
