from flask import Flask,Blueprint, render_template
from controllers.cachorro import *


app = Flask(__name__)
app.register_blueprint(cachorro)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=-True)