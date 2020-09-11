from controler import app

@app.route("/ping")
def pong():
    return "pong"