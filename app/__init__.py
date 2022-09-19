from config import Config
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(render_as_batch=True)

def create_app(config_class: Config):
    app = Flask(__name__)
    load_dotenv()
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app
