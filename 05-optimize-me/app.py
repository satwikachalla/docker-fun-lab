from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from " + os.environ.get("APP_NAME", "Docker") + " app"


@app.route("/health")
def health():
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
