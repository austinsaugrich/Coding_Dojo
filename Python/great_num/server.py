from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'hey'

number = random.randint(1, 100)


def guess_count():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return session['count']


def reset():
    global number
    num = number
    count = session['count']
    session['count'] = 0
    number = random.randint(1, 100)
    print(f'the number you need to guess is {number}')
    return num, count


@app.route('/')
def show_index():
    return render_template('index.html',)


@app.route('/guess', methods=['POST'])
def guess():
    guess_count()
    if session['count'] > 4:
        return redirect('/lose')
    num = int(request.form['num'])
    print(f'your guess was {num}')
    if num > number:
        return redirect('/high')
    elif num < number:
        return redirect('/low')
    else:
        if num == number:
            return redirect('/correct')


@app.route('/high')
def high():
    return render_template('high.html')


@app.route('/low')
def low():
    return render_template('low.html')


@app.route('/lose')
def lose():
    num, count = reset()
    return render_template('lose.html', number=num, count=count)


@app.route('/correct')
def correct():
    num, count = reset()
    return render_template('correct.html', number=num, count=count)


if __name__ == '__main__':
    print(f'the number you need to guess is {number}')
    app.run(debug=True)
