from flask import Blueprint, jsonify,request
from ..models.role import Role
app = Blueprint("roles", __name__)



@app.route('/roles',methods=['GET'])
def get_user():
    query_params = request.args.to_dict()
    roles = Role.list_by(query_params)
    return jsonify([r.serialize() for r in roles])


@app.route("/roles", methods=["POST"])
def create():
    role = Role.create(**request.json)
    return jsonify(role.serialize())
