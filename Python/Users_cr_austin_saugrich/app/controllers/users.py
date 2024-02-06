from app import app
from flask import Flask, session, render_template, request, redirect
from app.models.user import User

Users = [
    {
        'id': 2312,
        'first_name': 'first',
        'last_name': 'last',
        'email': 'email'
    }
]


@app.route('/')
def hello_world():
    print('hello world')
    return render_template('index.html', users=User.get_all())


@app.route('/users/new')
def add_user_form():
    return render_template('add.html')


@app.route('/users/new', methods=['POST'])
def add_user():
    User.add(request.form)
    return redirect('/')
