import json
import os
from flask import Flask, request, render_template, Blueprint


bp = Blueprint('esp', __name__, static_folder='static')

@bp.route("/esp")
def index():
    return render_template("esp/index.html")


@bp.route("/_led")
def _led():
    state = request.args.get("state")
    s = {
        "led" : state
    }

    fname = os.path.join(bp.static_folder, "states.json")

    with open(fname, "w") as outfile:
        json.dump(s, outfile)

    return "succes"

@bp.route("/read")
def readJSON():
    fname = os.path.join(bp.static_folder, "states.json")

    with open(fname, "r") as openfile:
        json_obj = json.load(openfile)

    print(json_obj['led'])



    return json_obj['led']



