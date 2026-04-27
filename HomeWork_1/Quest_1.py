from flask import Flask

app = Flask(__name__)

@app.route('/') # Ошибка была тут потому что оно передавало пустой знак.
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
