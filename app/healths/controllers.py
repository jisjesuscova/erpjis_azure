from flask import Blueprint, render_template, redirect, request, url_for
from app.models.models import HealthModel
from app.healths.health import Health

health = Blueprint("health", __name__)

@health.before_request
def constructor():
   pass

@health.route("/master_data/health/create", methods=['GET'])
def create():

   return render_template('master_data/health/health_create.html')

@health.route("/master_data/health", methods=['GET'])
@health.route("/master_data/health/<int:page>", methods=['GET'])
def index(page=1):
   return render_template('master_data/health/health.html', health = HealthModel.query.paginate(page=page, per_page=20, error_out=False))
@health.route("/master_data/health/store", methods=['POST'])
def store():
   Health.store(request.form)

   return redirect(url_for('health.index'))


@health.route("/master_data/health/edit/<int:id>", methods=['GET'])
@health.route("/master_data/health/edit", methods=['GET'])
def edit(id):
   health = Health.get(id)

   return render_template('master_data/health/health_edit.html', health = health, id = id)

@health.route("/master_data/health/<int:id>", methods=['POST'])
@health.route("/master_data/health", methods=['POST'])
def update(id):
   Health.update(request.form, id)

   return redirect(url_for('health.index'))

@health.route("/master_data/health/delete/<int:id>", methods=['GET'])
@health.route("/master_data/health/delete", methods=['GET'])
def delete(id):
   Health.delete(id)

   return redirect(url_for('health.index'))
