from flask import render_template, redirect, request, url_for
from application import app, db
from application.forms import LoginForm, LocationForm, Feedback
from flask import flash
from flask_sqlalchemy import SQLAlchemy #from sqlalchemy library import class sqlalchemy
from flask_login import current_user, login_user, logout_user, login_required
from application.models import User
from werkzeug.urls import url_parse
from application.forms import RegistrationForm

@app.route('/') #create an address for the website
@app.route('/home')
@login_required
def home(): #call a function home()
    return render_template('home.html', title='Home Page') #from that function, return home.html and variables

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/location', methods = ['GET', 'POST'])
def location():
    return render_template('location.html')

@app.route('/restaurants', methods = ['GET', 'POST'])
def restaurants():
    return render_template('restaurants.html')

@app.route('/select_order', methods = ['GET','POST'])
def select_order():
    return render_template('select_order.html')

@app.route('/feed_back', methods = ['GET','POST'] )
def feed_back():
    form = Feedback()
    if form.validate_on_submit():
        pass
    return render_template('feed_back.html',form = form) 

@app.route('/confirm', methods = ['GET','POST'])
def mobile_payment():
    order1 = request.form.get('order1')
    order2 = request.form.get('order2')
    order3 = request.form.get('order3')
    order4 = request.form.get('order4')
    order5 = request.form.get('order5')
    return render_template('mobile_payment.html', order1=order1, order2=order2, order3=order3, order4=order4, order5=order5)
    
@app.route('/finish', methods = ['GET', 'POST'])
def finish():
    return render_template('finish.html')
    
@app.route('/notifications', methods = {'GET', 'POST'})
def notifs():
    return render_template('notifs.html')


@app.route('/categories', methods = ['GET', 'POST'])
def categories():
    location = request.form.get('location')
    radius = request.form.get('radius')
    return render_template('Categories.html', location=location, radius=radius)

