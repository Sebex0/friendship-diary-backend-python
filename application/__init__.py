"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import logging

# Database variable
db = SQLAlchemy()

def create_app():
    # Construct the core application
    app = Flask(__name__, instance_relative_config=False)

    # Apply the configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():

        # Import parts of our application
        from .dashboard import routes
        from .auth import routes
        from .memories import routes
        from .friends import routes
        from .users import routes

        # Register Blueprints
        app.register_blueprint(dashboard.routes.main_bp)
        app.register_blueprint(auth.routes.auth_bp)
        app.register_blueprint(memories.routes.memories_bp)
        app.register_blueprint(friends.routes.friends_bp)
        app.register_blueprint(users.routes.users_bp)

        # Create database models
        db.create_all()

        return app
