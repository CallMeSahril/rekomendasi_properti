from flask import Blueprint, render_template

penjelasan_bp = Blueprint("penjelasan_bp", __name__, url_prefix="/admin")

@penjelasan_bp.route("/penjelasan")
def penjelasan():
    return render_template("admin/penjelasan.html")
