import os
import sys
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True, port=8080)