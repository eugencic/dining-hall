from flask import Flask

# Create a Flask object called app
app = Flask(__name__)

# App route
@app.route('/distribution')

def print_test():
    print(f"Test run of the server")
    
def run_dinninghall():
    print_test()
    app.run(host = '0.0.0.0', port = 3000, debug = True)

if __name__ == '__main__':
    run_dinninghall()