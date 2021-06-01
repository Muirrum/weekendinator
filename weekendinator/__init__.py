from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
db = SQLAlchemy()
login_manager = LoginManager()
migrator = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
            SQLALCHEMY_DATABASE_URI="postgresql://weekend:weekend@localhost/weekend",
            SECRET_KEY="badkey",
    )

    app.config.from_object("weekendinator.config")

    # Health Check
    @app.route('/health')
    def health():
        return "OK"

    db.init_app(app)
    login_manager.init_app(app)
    migrator.init_app(app, db)

    login_manager.login_view = "auth.login"
    login_manager.login_message = "You need to be logged in to view that page"

    # Init blueprints
    from weekendinator import auth
    app.register_blueprint(auth.bp)

    return app
