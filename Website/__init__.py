from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
DB_NAME='database.db'
# Improved configuration (consider using environment variables)
app_config = {
    'SECRET_KEY': 'heqpoc gadjhhjhj',  # Replace with a strong secret key
    'SQLALCHEMY_DATABASE_URI': f'sqlite:///{DB_NAME}',  # Replace DB_NAME with your filename
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
}

def create_app():
    app = Flask(__name__)
    app.config.update(app_config)

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Post

    # Create tables outside the context for reliable execution
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")

    return app