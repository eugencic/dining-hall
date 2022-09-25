from flask import Flask, request
from clientService.client import Client
from clientService.waiter import Waiter
from threading import Thread
from components.waiters import waiters

# Create a Flask object called app
app = Flask(__name__)

# Array to store the threads
threads = []

# App route
@app.route('/distribution', methods = ['GET', 'POST'])

def distribution():
    data = request.get_json()
    print(f'Order nr.{data["order_id"]} is served to table nr.{data["table_id"]}\n')
    return {'success': True}

def run_dinninghall():
    dining_hall_thread = Thread(target=lambda: app.run(host = '0.0.0.0', port = 3000, debug = False, use_reloader = False), daemon = True)
    dining_hall_thread.start()
    # Create thread Client
    client_thread = Client()
    # Add the thread to the array
    threads.append(client_thread)
    for _, waiter in enumerate(waiters):
        # Create Waiter threads
        waiter_thread = Waiter(waiter)
        # Add the thread to the list
        threads.append(waiter_thread)
    # Start the threads
    for thread in threads:
        thread.start()
    # Wait for the threads to complete    
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    run_dinninghall()