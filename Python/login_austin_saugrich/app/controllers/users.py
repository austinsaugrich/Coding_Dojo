from app import app
from flask_bcrypt import Bcrypt
from flask import Flask, session, render_template, request, redirect, flash
from app.models.user import User

bcrypt = Bcrypt(app)


@app.route('/')
def show_reg_form():
    return render_template('login.html')


@app.route('/register', methods=['POST'])
def add_new_user():
    if not User.validate_user_info(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }

    user_id = User.add(data)
    session['user_id'] = user_id
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    if not User.validate_user_login(request.form):
        return redirect('/')
    data = {'email': request.form['email']}
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash('No account found', 'login')
        return redirect('/')

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email/Password', 'login')
        return redirect('/')

    session['user_id'] = user_in_db.id

    return redirect('/dashboard')


@app.route('/dashboard')
def show_dashboard():
    id = session['user_id']
    return render_template('dashboard.html', user=User.get_by_id(id))


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
