from app import app
from flask import Flask, session, render_template, request, redirect
from app.models.ninja import Ninja
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
    return render_template('view.html', dojo=Dojo.get_by_id(id), all_ninja=Ninja.get_all(id))


@app.route('/new/ninja')
def add_ninja_form():
    return render_template('newninja.html', all_dojos=Dojo.get_all())


@app.route('/new/ninja', methods=['POST'])
def add_ninja():
    Ninja.add_ninja(request.form.to_dict())
    id = request.form['dojo_id']
    return redirect(f'/dojos/{id}')
