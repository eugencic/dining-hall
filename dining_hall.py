from flask import Flask
from threading import Thread
import random
import components.tables as tables
import components.foods as menu

# Create a Flask object called app
app = Flask(__name__)

# App route
@app.route('/distribution')

def run_dinninghall():
    app.run(host = '0.0.0.0', port = 3000, debug = True)

if __name__ == '__main__':
    run_dinninghall()