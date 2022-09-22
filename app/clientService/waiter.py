from threading import Thread
from components.tables import *
from components.orders import order_queue
import requests
import time
import threading
import random

time_unit = 1

# Customized Waiter class extending the Thread class
class Waiter(Thread):
    def __init__(self, data, *args, **kwargs):
        # Access methods of the base class
        super(Waiter, self).__init__(*args, **kwargs)
        self.daemon = True
        self.id = data['id']
        self.name = data['name']

    # Represent the thread's activity
    def run(self):
        while True:
            # Execute the function to take an order
            self.take_order()

    # Method to make an order
    def take_order(self):
        # Handling exceptions
        try:
            # Get order from the order queue
            order = order_queue.get()
            order_queue.task_done()
            # Take the table that made the order by table id 
            table_id = next((id for id, table in enumerate(tables) if table['id'] == order['table_id']), None)
            # Detailed message that the waiter took the order
            print(f'Table nr.{order["table_id"]}. Waiter {threading.current_thread().name} is taking the order nr.{order["id"]}. It has the priority {order["priority"]}, and foods: {order["items"]}.\n')
            # Change the state of the table
            tables[table_id]['state'] = table_state2
            # Execution time
            time.sleep(random.randint(2, 4) * time_unit)
            # Put the order data in a dictionary
            payload = dict({'order_id': order['id'], 'table_id': order['table_id'], 'waiter_id': self.id, 'items': order['items'], 'priority': order['priority'], 'max_wait': order['max_wait'], "pick_up_time": time.time()})
            requests.post('http://localhost:8000/order', json = payload, timeout = 0.0001)
        # Exceptions
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            pass