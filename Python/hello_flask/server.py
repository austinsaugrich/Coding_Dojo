from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def show_box():
    return render_template('index.html')


@app.route('/play/<int:num>')
def num_of_boxes(num):
    return render_template('index.html', num=num)


@app.route('/play/<int:num>/<color>')
def color_of_boxes(color, num):
    return render_template('index.html', num=num, color=color)


if __name__ == "__main__":
    app.run(debug=True)
