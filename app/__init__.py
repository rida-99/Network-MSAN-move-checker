from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Create logs dir if not exists
    os.makedirs("app/logs", exist_ok=True)

    # Import and register blueprint
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
