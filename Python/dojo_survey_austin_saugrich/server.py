from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hey'


@app.route('/')
def show_index():
    return render_template('index.html',)


@app.route('/process', methods=['POST'])
def get_form():
    session['data'] = request.form
    return redirect('/result')


@app.route('/result')
def show_form():
    return render_template('result.html', name=session['data']['name'], location=session['data']['locations'], language=session['data']['languages'], comment=session['data']['comments'])


if __name__ == '__main__':
    app.run(debug=True)
