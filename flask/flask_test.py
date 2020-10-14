from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return(
        '''
    Welcome to our Kickstarter Project<br>
    Available Routes:<br>
    /analysis<br>
    /machine_learning<br>
    /map
    ''')

@app.route("/analysis")
def analysis():
    return(
        '''
   analysis
    ''')


@app.route("/machine_learning")
def machine_learning():
    return(
        '''
    
    /machine_learning
    ''')


@app.route("/map")
def map():
    return(
        '''
    
    /map
    ''')




if __name__ == "__main__":
    app.run()
