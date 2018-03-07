from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
from flask_mail import Mail 

application = Flask(__name__)

application.config['SECRET_KEY'] = 'thisisasecret'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskuser.db'
application.config['CSRF_ENABLED'] = True 
application.config['USER_ENABLE_EMAIL'] = True 
application.config['USER_APP_NAME'] = ' The Code Rebels'
application.config['USER_AFTER_REGISTER_ENDPOINT'] = 'user.login'
application.config.from_pyfile('config.cfg')

db = SQLAlchemy(application)
mail = Mail(application)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')
    email = db.Column(db.String(255), nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime())

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, application)

@application.route('/')
def index():
    return '<h1>This is the home page!</h1>'

@application.route("/pop_up_html")
def pop_up_html():
    return  render_template("/pop_up_html.html")

@application.route('/profile')
@login_required
def profile():
    return '<h1>This is the protected profile page!</h1>'

if __name__ == '__main__':
    application.run(debug=True) 