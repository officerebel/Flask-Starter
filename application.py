from flask import Flask

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

# from flask import Flask 
# from flask_sqlalchemy import SQLAlchemy 
# from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
# from flask_mail import Mail 

# application = Flask(__name__)

# application.config['SECRET_KEY'] = 'thisisasecret'
# application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskuser.db'
# application.config['CSRF_ENABLED'] = True 
# application.config['USER_ENABLE_EMAIL'] = True 
# application.config['USER_APP_NAME'] = ' The Code Rebels'
# application.config['USER_AFTER_REGISTER_ENDPOINT'] = 'user.login'
# application.config.from_pyfile('config.cfg')

# db = SQLAlchemy(application)
# mail = Mail(application)

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), nullable=False, unique=True)
#     password = db.Column(db.String(255), nullable=False, server_default='')
#     active = db.Column(db.Boolean(), nullable=False, server_default='0')
#     email = db.Column(db.String(255), nullable=False, unique=True)
#     confirmed_at = db.Column(db.DateTime())

# db_adapter = SQLAlchemyAdapter(db, User)
# user_manager = UserManager(db_adapter, application)

# @application.route('/')
# def index():
#     return '<h1>This is the home page!</h1>'

# @application.route("/pop_up_html")
# def pop_up_html():
#     return  render_template("/pop_up_html.html")

# @application.route('/profile')
# @login_required
# def profile():
#     return '<h1>This is the protected profile page!</h1>'

# if __name__ == '__main__':
#     application.run(debug=True) 