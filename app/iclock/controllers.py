from flask import Blueprint, render_template, request, make_response, jsonify
from flask_login import login_required
import sys
import os
import json
from textwrap import wrap
from datetime import datetime
from pprint import pprint

iclock = Blueprint("iclock", __name__)


@iclock.route("/clock", methods=["GET", "POST", "PATCH", "DELETE"])
def hello_world(path = ''):
    divider = "================================================================"
    j = request.get_json()

    print(divider)
    print(f"*** Received data at: {path}")

    print("\n** data:")
    print("\n".join(wrap(request.data.decode())))

    print("\n** form:")
    pprint(request.form)

    print("\n** json:")
    pprint(j)

    print(f"{divider}\n\n")

    return jsonify(
        {
            "endpoint": path,
            "data": request.data.decode("utf-8"),
            "form": request.form,
            "json": request.get_json(),
        }
    )
