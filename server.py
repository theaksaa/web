from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def receive():
    data = request.args.get("data")
    if data:
        print("Primljen podatak:", data, flush=True)  # flush da se vidi u Render logu
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
