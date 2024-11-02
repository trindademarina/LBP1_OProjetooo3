from flask import Flask, render_template
from controllers.controller import projeto

app = Flask(__name__)
app.secret_key = 'batataCmKetchup'
app.register_blueprint(projeto)


if __name__  == '__main__':
    app.run(debug=True)