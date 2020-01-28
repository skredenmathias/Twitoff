from flask import Flask

def create_app():
    '''Create and configure an instrance of the Flask application.'''
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Hello World!'
    
    return app
# $env:FLASK_APP = "hello.py