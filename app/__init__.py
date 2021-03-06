import os

from flask import Flask
from flask_pymongo import PyMongo

from app.api.v1.debug import debug_endpoint
from app.api.v1.services import services_endpoint
from app.api.v1.user import user_endpoint

frontend_dir = os.path.abspath("templates/")
static_dir = os.path.abspath("static/")

app = Flask(__name__, template_folder=frontend_dir, static_folder=static_dir)

app.register_blueprint(debug_endpoint, url_prefix="/api/v1/debug")
app.register_blueprint(services_endpoint, url_prefix="/api/v1/services")
app.register_blueprint(user_endpoint, url_prefix="/api/v1/user")

if "MONGODB_URI" in os.environ:
    app.config["MONGO_URI"] = os.environ["MONGODB_URI"]
    print("Using remote server")
else:
    app.config["MONGO_URI"] = "mongodb://localhost:27017/boop"
    print("Using local server")

mongo = PyMongo(app)
