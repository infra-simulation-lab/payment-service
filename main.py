from flask import Flask, jsonify
import uuid

app = Flask(__name__)

@app.route("/")
def make_payment():
    return jsonify({
        "status": "success",
        "payment_id": str(uuid.uuid4())
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
