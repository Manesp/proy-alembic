from flask import Blueprint, current_app
from models import NewUser


app = Blueprint("ping", __name__)


@app.route("/ping")
def ping():
    return "pong"

@app.route('/name',methods=['GET'])
NewUser()
    return "200"
