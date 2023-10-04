from flask import Blueprint, render_template, redirect, request, url_for
from app.models.models import ContractTypeModel
from app.contract_types.contract_type import ContractType

contract_type = Blueprint("contract_types", __name__)

@contract_type.before_request
def constructor():
   pass

@contract_type.route("/human_resources/contract_type/create", methods=['GET'])
def create():

   return render_template('master_data/contract_types/contract_types_create.html')

@contract_type.route("/master_data/contract_types", methods=['GET'])
@contract_type.route("/master_data/contract_types/<int:page>", methods=['GET'])
def index(page=1):
   return render_template('master_data/contract_types/contract_types.html', contract_types = ContractTypeModel.query.paginate(page=page, per_page=20, error_out=False))

@contract_type.route("/master_data/contract_type/store", methods=['POST'])
def store():
   contract_type = ContractType.store(request.form)

   return redirect(url_for('contract_types.index'))

@contract_type.route("/master_data/contract_type/<int:id>", methods=['GET'])
@contract_type.route("/master_data/contract_type", methods=['GET'])
def show(id):
   contract_type = ContractType.get(id)

   return render_template('master_data/contract_types/contract_types_update.html', contract_type = contract_type, id = id)

@contract_type.route("/master_data/contract_type/<int:id>", methods=['POST'])
@contract_type.route("/master_data/contract_type", methods=['POST'])
def update(id):
   ContractType.update(request.form, id)

   return redirect(url_for('contract_types.index'))

@contract_type.route("/master_data/contract_type/delete/<int:id>", methods=['GET'])
@contract_type.route("/master_data/contract_type/delete", methods=['GET'])
def delete(id):
   ContractType.delete(id)

   return redirect(url_for('contract_types.index'))
