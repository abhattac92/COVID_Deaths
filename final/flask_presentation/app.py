from flask import Flask, render_template

app = Flask(__name__)


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


@app.route('/map_test')
def map_test():
    return render_template('map_test.html')


if __name__ == "__main__":
    app.run(debug=True)
