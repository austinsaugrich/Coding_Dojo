from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hey'


@app.route('/')
def show_doc():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1

    return render_template("index.html", count=session['count'])


@app.route('/add2')
def add_one():
    session['count'] += 1
    return redirect('/')


@app.route('/destroy_session')
def reset_page():
    session['count'] = 0
    return redirect('/')


if __name__ == '__main__':

    app.run(debug=True)
