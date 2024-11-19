from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        from .routes import bp as routes_bp
        app.register_blueprint(routes_bp)
        db.create_all()  # Crear las tablas si no existen

    return app
