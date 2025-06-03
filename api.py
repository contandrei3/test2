from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/is_even", methods=["GET"])
def is_even():
    number_str = request.args.get("number")
    if number_str is None:
        return jsonify({"error": "No number provided"}), 400

    try:
        number = int(number_str)
        return jsonify({"even": number % 2 == 0})
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Folosește PORT de la Railway sau default 10000
    app.run(host="0.0.0.0", port=port)
