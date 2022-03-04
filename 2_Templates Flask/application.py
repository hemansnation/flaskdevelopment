from crypt import methods
from flask import Flask, render_template, request

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

@app.route('/signin')
def sign():
    return render_template('signin.html')

# @app.route('/process', methods=['POST'])
# def process():
#     name = request.form['username']
#     return "<h1>" + str(name) + "</h1>"

@app.route('/process', methods=['POST'])
def process():
    name = request.form['username']
    return render_template('example.html', goa = name)


if __name__ == "__main__":
    app.run(debug=True,port=5501)