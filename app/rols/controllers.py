from flask import Blueprint, render_template
from flask_login import login_required
from app.models.models import Rol
from app import app, rols

rols = Blueprint("rols", __name__)

@rols.route("/rols", methods=['GET'])
def rols(page=1):
    pass