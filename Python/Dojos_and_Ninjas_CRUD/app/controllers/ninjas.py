from app import app
from flask import Flask, session, render_template, request, redirect
from app.models.ninja import Ninja
# Should I import this model here for line 10, or repeat myself and make a new function ?
from app.models.dojo import Dojo


@app.route('/new/ninja')
def add_ninja_form():
    return render_template('newninja.html', all_dojos=Dojo.get_all())


@app.route('/new/ninja', methods=['POST'])
def add_ninja():
    Ninja.add_ninja(request.form.to_dict())
    id = request.form['dojo_id']
    return redirect(f'/dojos/{id}')
