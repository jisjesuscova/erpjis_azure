from flask import Blueprint, render_template

civil_state = Blueprint("civil_states", __name__)

@civil_state.before_request
def constructor():
   pass

@civil_state.route("/master_data/civil_states", methods=['GET'])
def index():
   return 