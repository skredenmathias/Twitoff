'''Entry point for TwitOff'''
from .app import create_app
from flask_debug import Debug

APP = create_app()

Debug(APP)

if __name__ == "__main__":
    APP.run(debug=True)