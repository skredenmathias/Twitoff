# from decouple import config
# # from dotenv import load_dotenv
# from flask import Flask, render_template, request
# from .models import DB, User
# from .twitter import add_or_update_user

# # load_dotenv()

# def create_app():
#     '''Create and configure an instrance of the Flask application.'''
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL') # 'sqlite:///db.sqlite3'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     DB.init_app(app)

#     @app.route('/')
#     def root():
#         DB.create_all()
#         return render_template('base.html', title='Home', users=User.query.all())
    
#     @app.route('/user', methods=['POST'])
#     @app.route('/user/<name>', methods=['GET'])
#     def user(name=None, message=''):
#         name = name or request.values['user_name']
#         try:
#             if request.method == 'POST':
#                 add_or_update_user(name)
#                 message = f'User {name} successfully added'
#             tweets = User.query.filter(User.name==name).one().tweets
#         except Exception as e:
#             message = f'Error while trying to add user {name}: {e}'
#             tweets = []
#         return render_template('user.html', title=name, message=message,
#         tweets=tweets)

#     @app.route('/reset')
#     def reset():
#         DB.drop_all()
#         DB.create_all()
#         return render_template('base.html', title='Reset database!')

#     return app

from decouple import config
from flask import Flask, render_template, request

from .models import DB, User
from .twitter import add_or_update_user


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        DB.create_all()
        return render_template('base.html', title='Home', users=User.query.all())

    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=''):
        name = name or request.values['username']
        try:
            if request.method == "POST":
                add_or_update_user(name)
                message = f'User {name} successfully added!'
            tweets = User.query.filter(User.name==name).one().tweets
        except Exception as e:
            message = f'Error while try to add user {name}: {e}'
            tweets = []
        return render_template('user.html', title=name, message=message, tweets=tweets)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset database!')

    return app