from datetime import datetime

from flask import Flask
from flask import render_template

from config import config

app = Flask(__name__)


@app.context_processor
def inject_now():
    return {"now": datetime.utcnow()}


@app.route("/")
def home():
    social_media_info = config.get_social_media_info()

    return render_template("home.html", **social_media_info)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
