from threading import Thread
from components.tables import *
from components.orders import order_queue
import requests

time_unit = 1

# Customized Waiter class extending the Thread class
class Waiter(Thread):
    def __init__(self, *args, **kwargs):
        # Access methods of the base class
        super(Waiter, self).__init__(*args, **kwargs)

    # Represent the thread's activity
    def run(self):
        while True:
            # Execute the function to take an order
            self.take_order()

    # Method to make an order
    def take_order(self):
        # Get order from the order queue
        order = order_queue.get()
        order_queue.task_done()
        # Take the table that made the order by table id 
        table_id = next((id for id, table in enumerate(tables) if table['id'] == order['table_id']), None)
        # Detailed message that the waiter took the order
        print(f'Table nr.{order["table_id"]}. The waiter is taking the order nr.{order["id"]}. It has the priority {order["priority"]}, and foods: {order["items"]}.')
        # Change the state of the table
        tables[table_id]['state'] = table_state2
        # Put the order data in a dictionary
        payload = dict({'table_id': order['table_id'], 'order_id': order['id'], 'items': order['items'], 'priority': order['priority']})
        requests.post('http://localhost:8000/order', data = payload, timeout = 0.0001)