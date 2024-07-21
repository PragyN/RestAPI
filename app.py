from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/route1', methods=['GET'])
def route1():
    return 'welcome to route 1'

if __name__ == '__main__':
    app.run(debug=True, port=int("3000"), host='0.0.0.0')
