from datetime import datetime

from config import config
from flask import Flask
from flask import render_template
from flask_caching import Cache
from flask_compress import Compress

app = Flask(__name__)
cache = Cache(app, config={"CACHE_TYPE": "simple"})
Compress(app)


@app.context_processor
def inject_now():
    return {"now": datetime.utcnow()}


@app.route("/")
@cache.cached(timeout=60)
def home():
    social_media_info = config.get_social_media_info()

    return render_template("home.html", **social_media_info)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
