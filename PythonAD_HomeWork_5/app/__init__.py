from flask import Flask
from app.routers.questions import questions_bp
from app.routers.responses import responses_bp
from app.routers.categories import categories_bp
from config import DevelopmentConfig
from app.extensions import db, migrate
import app.models


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(questions_bp, url_prefix='/questions')
    app.register_blueprint(responses_bp, url_prefix='/responses')
    app.register_blueprint(categories_bp, url_prefix='/categories')

    db.init_app(app)
    migrate.init_app(app, db)

    return app
