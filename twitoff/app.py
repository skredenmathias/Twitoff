from decouple import config
from dotenv import load_dotenv
from flask import Flask, render_template
from .models import DB, User

load_dotenv()

def create_app():
    '''Create and configure an instrance of the Flask application.'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL') # 'sqlite:///db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='Welcome to the Jam', user = User.query.all())
    return app