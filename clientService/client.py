from threading import Thread
import time
import random
from components.tables import *
from components.foods import menu
from components.orders import order_queue

# Customized Clients class extending the Thread class
class Clients(Thread):
    def __init__(self, *args, **kwargs):
        # Access methods of the base class
        super(Clients, self).__init__(*args, **kwargs)

    # Represent the thread's activity
    def run(self):
        # Continuous threading of creating objects
        while True:
            # Delay the execution of the function for 5 seconds
            time.sleep(5)
            # Execute the function to create an order
            self.generate_order()

    # Method to generate an order
    def generate_order(self):
        # Return the next free table and it's index from the list of tables
        # Iterate through the tables and return nothing by default, when the iteration ends
        (table_id, table) = next(((index, table) for index, table in enumerate(tables) if tables[index]['state'] == table_state1), (None, None))
        # Check if there is a free table
        if table_id is not None:
            # Random order id
            order_id = int(random.random() * random.random() / random.random() * 1000)
            # Create an array to store the chosen foods id's
            # The client can order up to 10 foods
            chosen_foods = random.sample(range(1, len(menu) + 1), random.randint(1, 10))
            # Random order priority
            order_priority = random.randint(1, 5)
            # Create the order
            order = {'table_id': table['id'], 'id': order_id, 'items': chosen_foods, 'priority': order_priority}
            # Put the order in the orders queue
            order_queue.put(order)