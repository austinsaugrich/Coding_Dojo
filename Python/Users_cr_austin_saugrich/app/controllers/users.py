from app import app
from flask import Flask, session, render_template, request, redirect
from app.models.user import User


@app.route('/')
def hello_world():
    print('hello world')
    return render_template('index.html', users=User.get_all())


@app.route('/users/new')
def add_user_form():
    return render_template('add.html')


@app.route('/users/new', methods=['POST'])
def add_user():
    newuser = User.add(request.form)
    return redirect(f'/user/{newuser}')


@app.route('/edit/user/<int:id>')
def edit_user_form(id):
    return render_template('edit.html', user=User.get_by_id(id))


@app.route('/edit/user', methods=['POST'])
def edit_user():
    User.edit(request.form)
    return redirect(f'/user/{request.form["id"]}')


@app.route('/user/<int:id>')
def view_user(id):
    return render_template('view.html', user=User.get_by_id(id))


@app.route('/user/delete/<int:id>')
def delete_user(id):
    User.delete(id)
    return redirect('/')
