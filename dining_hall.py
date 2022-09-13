from flask import Flask
from clientService.client import Client
from clientService.waiter import Waiter

# Create a Flask object called app
app = Flask(__name__)

# Array to store the threads
threads = []

# App route
@app.route('/distribution')

def run_dinninghall():
    app.run(host = '0.0.0.0', port = 3000, debug = False)
    # Create thread Client
    client_thread = Client()
    # Add the thread to the array
    threads.append(client_thread)
    # Create thread Waiter
    waiter_thread = Waiter()
    # Add the thread to the list
    threads.append(waiter_thread)
    
    # Start the threads
    for th in threads:
        th.start()
    # Wait for the threads to complete    
    for th in threads:
        th.join()

if __name__ == '__main__':
    run_dinninghall()