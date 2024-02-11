from app import app
from flask import Flask, session, render_template, request, redirect
from app.models.dojo import Dojo


@app.route('/')
def dashboard():
    return render_template('dashboard.html', dojos=Dojo.get_all())


@app.route('/add/dojo', methods=['POST'])
def add_dojo():
    Dojo.add_dojo(request.form)
    return redirect('/')


@app.route('/dojos/<int:id>')
def view_dojo(id):
    return render_template('view.html', dojo=Dojo.get_dojo_with_ninjas(id))
