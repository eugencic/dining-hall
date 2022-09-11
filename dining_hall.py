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
        
    # Represent the thread's activity
    def run(self):
        # Continuous threading of creating objects
        while True:
            self.create_order()   
             
    # Convert a function to be a static method, which does not receive an implicit first argument
    @staticmethod
    # Method to generate an order
    def generate_order():
        # Return the next table and it's index from the list of tables
        # Iterate through the tables and return nothing by default, when the iteration ends
        (table_id, table) = next(((index, table) for index, table in enumerate(tables)), (None, None))
        # Check if there is a table
        if table_id is not None:
            # Create an array to store the foods that the client will choose
            chosen_foods = []
            # The client can choose up to 10 items
            for _ in range(random.randint(1, 10)):
                # Select a food from the menu
                choice = random.choice(menu)
                # Add the id of the food to the array
                chosen_foods.append(choice['id'])
            # Generate an id of the order
            order_id = int(random.randint(1, 1000) * random.randint(1, 1000))
            # Create the order
            order = {'table_id': table['id'], 'id': order_id, 'items': chosen_foods, 'priority': random.randint(1, 5)}
   
def run_dinninghall():
    app.run(host = '0.0.0.0', port = 3000, debug = True)

if __name__ == '__main__':
    run_dinninghall()