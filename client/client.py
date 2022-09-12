from threading import Thread
import random
import components.tables as tables
import components.foods as menu
import components.orders as orders

# Customized Clients class extending the Thread class
class Clients(Thread):
    def __init__(self, *args, **kwargs):
        # Access methods of the base class
        super(Clients, self).__init__(*args, **kwargs)
        
    # Represent the thread's activity
    def run(self):
        # Continuous threading of creating objects
        while True:
            self.generate_order()   
             
    # Convert a function to be a static method, which does not receive an implicit first argument
    @staticmethod
    # Method to generate an order
    def generate_order():
        # Return the next table and it's index from the list of tables
        # Iterate through the tables and return nothing by default, when the iteration ends
        (table_id, table) = next(((index, table) for index, table in enumerate(tables.tables)), (None, None))
        # Check if there is a table
        if table_id is not None:
            # Random order id
            order_id = int(random.random() * random.random() / random.random() * 1000000)
            # Create an array to store the chosen foods id's
            # The client can order up to 10 foods
            chosen_foods = random.sample(range(1, len(menu) + 1), random.randint(1, 10))
            # Random order priority
            order_priority = random.randint(1, 5)
            # Create the order
            order = {'table_id': table['id'], 'id': order_id, 'items': chosen_foods, 'priority': order_priority}
            # Put the order in the orders queue
            orders.order_queue.put(order)