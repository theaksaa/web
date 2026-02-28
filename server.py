  GNU nano 7.2                                            server.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def receive():
    data = request.args.get("data")
    if data:
        print("Data:", data)
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
