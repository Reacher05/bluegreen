from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    color = os.getenv("APP_COLOR", "DEFAULT")
    feature_new_api = os.getenv("FEATURE_NEW_API", "false").lower() == "true"

    if feature_new_api:
        return jsonify({
            "status": "ok",
            "version": color,
            "new_feature_enabled": True,
            "data": [i**2 for i in range(5)]
        })
    else:
        return color

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)