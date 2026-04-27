from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/user/<user>')
def hello_user(user):
    return f'Hello, {user}!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')