from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # permite accesul din Thunkable sau browser

@app.route("/is_even", methods=["POST"])
def is_even():
    data = request.get_json()
    if not data or "number" not in data:
        return jsonify({"error": "Trimite un câmp 'number'"}), 400

    number = data["number"]
    if not isinstance(number, int):
        return jsonify({"error": "Valoarea trebuie să fie un număr întreg"}), 400

    este_par = number % 2 == 0
    return jsonify({"par": este_par})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
