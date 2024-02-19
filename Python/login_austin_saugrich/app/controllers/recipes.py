from app import app
from flask import Flask, session, render_template, request, redirect, flash
from app.models.recipe import Recipe
from app.models.recipe import User


@app.route('/create')
def show_recipe_form():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('create.html')


@app.route('/create', methods=['POST'])
def get_recipe_form():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_form(request.form):
        return redirect('/create')
    data = {
        'user_id': session['user_id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date': request.form['date'],
        'under': request.form['under'],
    }
    Recipe.add(data)
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('dashboard.html', recipes=Recipe.get_all(), users=User.get_by_id(session['user_id']))


@app.route('/recipe/edit/<int:id>')
def show_edit_form(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id(id)
    print(recipe.__dict__)
    if session['user_id'] != recipe.user:
        return redirect('/dashboard')
    return render_template('edit.html', recipe=Recipe.get_by_id(id))


@app.route('/edit/<int:id>', methods=['POST'])
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date': request.form['date'],
        'under': request.form['under'],
    }
    Recipe.edit(data)
    return redirect('/dashboard')


@app.route('/recipe/delete/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    Recipe.delete(id)
    return redirect('/dashboard')


@app.route('/recipe/<int:id>')
def view_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    return render_template('view.html', users=User.get_by_id(session['user_id']), recipe=Recipe.get_by_id(id))
