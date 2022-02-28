from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from flask app"

@app.route('/home')
def home():
    return "<h1>Welcome User</h1>"

@app.route('/example')
def example():
    return render_template('example.html')


if __name__ == "__main__":
    app.run(debug=True,port=5501)