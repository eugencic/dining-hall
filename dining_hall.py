from flask import Flask
from threading import Thread
import random
import components.tables as tables
import components.foods as menu

# Create a Flask object called app
app = Flask(__name__)

# App route
@app.route('/distribution')

# Customized Clients class extending the Thread class
class Clients(Thread):
    def __init__(self, *args, **kwargs):
        # Access methods of the base class
        super(Clients, self).__init__(*args, **kwargs)
        
def run_dinninghall():
    app.run(host = '0.0.0.0', port = 3000, debug = True)

if __name__ == '__main__':
    run_dinninghall()