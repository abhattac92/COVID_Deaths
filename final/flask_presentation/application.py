from flask import Flask, render_template

application = app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/data_pro')
def data_pro():
    return render_template('data_pro.html')


@app.route('/machine')
def machine():
    return render_template('machine.html')


@app.route('/app_k')
def app_k():
    return render_template('app_k.html')


@app.route('/app_const')
def app_const():
    return render_template('app_const.html')


if __name__ == "__main__":
    app.run(debug=True)
