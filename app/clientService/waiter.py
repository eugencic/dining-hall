from threading import Thread
from components.tables import *
from components.orders import *
import requests
import time
import threading
import random

time_unit = 1
orders_rating = []

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

    # Method to take an order
    def take_order(self):
        # Handling exceptions
        try:
            # Get order from the order queue
            order = order_queue.get()
            order_queue.task_done()
            # Take the table that made the order by table id
            table_id = None
            for id, table in enumerate(tables):
                 if table['id'] == order['table_id']:
                     table_id = id
            # Detailed message that the waiter took the order
            print(f'Table nr.{order["table_id"]}. Waiter {threading.current_thread().name} is taking the order nr.{order["id"]}. It has the priority {order["priority"]}, and foods: {order["items"]}\n')
            # Change the state of the table
            tables[table_id]['state'] = table_state3
            # Execution time
            time.sleep(random.randint(2, 4) * time_unit)
            # Put the order data in a dictionary
            payload = dict({'order_id': order['id'], 'table_id': order['table_id'], 'waiter_id': self.id, 'items': order['items'], 'priority': order['priority'], 'max_wait': order['max_wait'], "pick_up_time": time.time()})
            # Send the order to the kitchen
            requests.post('http://localhost:8000/order', json = payload, timeout = 0.0001)
            #requests.post('http://kitchen:8000/order', json = payload, timeout = 0.0001)
        # Exceptions
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            pass
        
    # Method to serve the order
    def serve_order(self, sent_order):
        # Check if the sent order is the same order that what was requested
        received_order = None
        for index, order in enumerate(orders):
            if order['id'] == sent_order['order_id']:
                received_order = order
        # Check if the items of the order are the same as requested
        if received_order is not None and received_order['items'].sort() == sent_order['items'].sort():
            # Update the table state
            table_id = None
            for index, table in enumerate(tables):
                if table['id'] == sent_order['table_id']:
                    table_id = index
            tables[table_id]['state'] = table_state4
            # Time from when the order was picked up
            order_pick_up = int(sent_order['pick_up_time'])
            # Time for when the order is served
            order_serving = int(time.time())
            # Calculate the total time of the order till it was served
            order_total_time = order_serving - order_pick_up
            # Calculate the order rating
            order_stars = {'order_id': sent_order['order_id']}
            if sent_order['wait_time'] > order_total_time:
                order_stars['star'] = 5
            elif sent_order['wait_time']* 1.1 > order_total_time:
                order_stars['star'] = 4
            elif sent_order['wait_time'] * 1.2 > order_total_time:
                order_stars['star'] = 3
            elif sent_order['wait_time'] * 1.3 > order_total_time:
                order_stars['star'] = 2
            elif sent_order['wait_time'] * 1.4 > order_total_time:
                order_stars['star'] = 1
            else:
                order_stars['star'] = 0
            # Restaurant reputation 
            orders_rating.append(order_stars)
            calculate_stars = sum(stars['star'] for stars in orders_rating)
            average = float(calculate_stars / len(orders_rating))
            # Create the served order dict
            served_order = {
                'order_id': sent_order['order_id'], 
                'table_id': sent_order['table_id'], 
                'waiter_id': sent_order['waiter_id'],
                'items': sent_order['items'], 
                'priority': sent_order['priority'],
                'wait_time': sent_order['wait_time'],
                'serving_time': order_total_time,
                'order_rating': order_stars,
                }
            # Message with the information of the served order
            print(
                f'Serving the order:\n'
                f'Order Id: {served_order["order_id"]}\n'
                f'Table Id: {served_order["table_id"]}\n'
                f'Waiter Id: {served_order["waiter_id"]}\n'
                f'Items: {served_order["items"]}\n'
                f'Priority: {served_order["priority"]}\n'
                f'Max Wait: {served_order["wait_time"]}\n'
                f'Waiting time: {served_order["serving_time"]}\n'
                f'Order rating: {served_order["order_rating"]}\n'
                f'Restaurant rating: {average}\n')
        # Exception if the order is not the same as requested
        else:
            raise Exception(f'There is a mistake. Provide the required order to costumer. Required: {received_order} Given: {sent_order}\n')