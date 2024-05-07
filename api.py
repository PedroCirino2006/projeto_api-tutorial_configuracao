from flask import Blueprint, jsonify, request

bp = Blueprint("api", __name__)

@bp.route("/", methods=("GET",))
def index():
    return jsonify({"status": 200, "message": "API Pedro"})

@bp.route("/aleatorios", methods=("GET",))
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

