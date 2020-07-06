from flask import Flask,render_template,jsonify,request,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect,CSRFError
from wtforms import StringField, PasswordField,BooleanField
from wtforms.validators import InputRequired,Email,Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models1 import *
from models2 import *
from models3 import *
from models4 import *

import os
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:567890@localhost:5432/project'
bootstrap = Bootstrap(app)
db=SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hostels")
def hostels():
    return render_template("hostels.html")

@app.route("/boys")
def boys():
    return render_template("boys.html")

@app.route("/girls")
def girls():
    return render_template("girls.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()  
    form.hostel.choices=[(hostel.number,hostel.hostel) for hostel in Hostels.query.filter_by(gender='M').all()]
    if request.method == 'POST':
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Users(name=form.name.data,username=form.username.data, email=form.email.data, password=hashed_password,phone=form.phone.data,gender=form.gender.data,hostel=form.hostel.data)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

@app.route('/signup/<gender>', methods=['GET', 'POST'])
def hos(gender):
    hostels = Hostels.query.filter_by(gender=gender).all()

    hostelarray=[]

    for hostel in hostels:
        hostelobj = {}
        hostelobj['number'] = hostel.number
        hostelobj['hostel'] = hostel.hostel
        hostelarray.append(hostelobj)

    return jsonify({'hostels' : hostelarray})


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/new',methods=['GET', 'POST'])
@login_required
def new():
    form = choiceform()
    form.hostel.choices=[(hostel.hostel,hostel.hostel) for hostel in Hostels.query.filter_by(gender=current_user.gender).all()]
    form.type.choices=[(hotel.type,hotel.type) for hotel in Hotels.query.filter_by(name='A')]
    form.sharing.choices=[(hotel.sharing,hotel.sharing) for hotel in Hotels.query.filter_by(name='A')]
    if request.method == 'POST':
        user=Choices(id=form.roll.data,hostel=form.hostel.data,type=form.type.data,sharing=form.sharing.data)
        db.session.add(user)
        db.session.commit()
        
        return '<h1> choice filled </h1>'
    return render_template('new.html', form=form)

@app.route('/new/<hostel>', methods=['GET','POST'])
def tape(hostel):
    hostels = Hotels.query.filter_by(name=hostel).all()

    hostelarray=[]

    for hostel in hostels:
        hostelobj = {}
        hostelobj['type'] = hostel.type
        hostelobj['sharing'] = hostel.sharing
        hostelarray.append(hostelobj)

    return jsonify({'hostels' : hostelarray})


if __name__ == '__main__':
    app.run(debug=True)