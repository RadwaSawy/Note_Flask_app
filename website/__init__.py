from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) # ???
    
    # secret key of the app
    app.config['SECRET_KEY'] = 'vbhdjkflfjh shdjkvv' # secure cookies related to the website
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    # Now the database is created and linked  
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # flask should redirect to log in screen if not logged in 
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id): 
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
             db.create_all()
