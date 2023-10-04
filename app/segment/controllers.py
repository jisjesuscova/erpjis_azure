from flask import Blueprint, render_template, redirect, request, url_for
from app.models.models import SegmentModel
from app.segment.segment import Segment

segment = Blueprint("segment", __name__)

@segment.before_request
def constructor():
   pass

@segment.route("/master_data/segment/create", methods=['GET'])
def create():

   return render_template('master_data/segment/segment_create.html')

@segment.route("/master_data/segment", methods=['GET'])
@segment.route("/master_data/segment/<int:page>", methods=['GET'])
def index(page=1):
   return render_template('master_data/segment/segment.html', segment = SegmentModel.query.paginate(page=page, per_page=20, error_out=False))
@segment.route("/master_data/segment/store", methods=['POST'])
def store():
   Segment.store(request.form)

   return redirect(url_for('segment.index'))


@segment.route("/master_data/segment/edit/<int:id>", methods=['GET'])
@segment.route("/master_data/segment/edit", methods=['GET'])
def edit(id):
   Segment = Segment.get(id)

   return render_template('master_data/segment/segment_edit.html', segment = segment, id = id)

@segment.route("/master_data/segment/<int:id>", methods=['POST'])
@segment.route("/master_data/segment", methods=['POST'])
def update(id):
   Segment.update(request.form, id)

   return redirect(url_for('segment.index'))

@segment.route("/master_data/segment/delete/<int:id>", methods=['GET'])
@segment.route("/master_data/segment/delete", methods=['GET'])
def delete(id):
   Segment.delete(id)

   return redirect(url_for('segment.index'))
