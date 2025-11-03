#!/usr/bin/env python3
#import flask from the flask module
from flask import Flask

# Create an instance of the Flask class
# __name__ tells Flask where to look for resources like templates and static files
app = Flask(__name__)

# ROUTE 1: Index/Home Page
# The @app.route decorator tells Flask what URL should trigger this function
# '/' means this function will handle requests to the root URL (home page)

@app.route('/')
def index():
    """
    This is the home page view function.
    When someone visits the base URL (/), this function runs.
    It returns HTML content that will be displayed in the browser.
    """
    return '<h1>Python Operations with Flask Routing and Views</h1>'
# ROUTE 2: Print String
# <string:parameter> creates a variable part of the URL
# The 'string' type converter ensures the parameter is treated as a string
# Whatever is in the URL after /print/ will be passed to the function as 'parameter'
@app.route('/print/<string:parameter>')
def print_string(parameter):
    """
    This view function takes a string from the URL and:
    1. Prints it to the console (server-side)
    2. Returns it to display in the browser (client-side)
    
    Example: /print/hello will print "hello" to console and show "hello" on the page
    """
    print(parameter) #prints to the server console
    return parameter #returns to the browser
# ROUTE 3: Count Numbers
# <int:parameter> creates a variable part that must be an integer
# Flask automatically converts the URL parameter to an integer

@app.route('/count/<int:parameter>')
def count(parameter):
    """
    This view function takes an integer and displays all numbers
    from 0 up to (but not including) that number, each on a separate line.
    
    Example: /count/5 will display:
    0
    1
    2
    3
    4
    """
    result=[] #create an empty list to store numbers

    # Loop from 0 to parameter-1

    for i in range(parameter):
        result.append(str(i)) #convert number to string and add to list
    # Join all numbers with newline characters and add a final newline
    return '\n'.join(result) + '\n'

# ROUTE 4: Math Operations
# Multiple parameters in the URL: <num1>/<operation>/<num2>
# All parameters are strings by default, so we'll convert numbers inside the function

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    """
    This view function performs mathematical operations on two numbers.
    It takes three parameters from the URL:
    - num1: first number
    - operation: the operation to perform (+, -, *, div, %)
    - num2: second number
    
    Example: /math/10/+/5 will return "15"
    Example: /math/10/div/2 will return "5.0"
    """
    # Convert string parameters to float numbers so we can do math
    num1 = float(num1)
    num2 = float(num2)
    
    # Use if/elif statements to determine which operation to perform
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':  # We use 'div' instead of '/' because '/' has special meaning in URLs
        result = num1 / num2
    elif operation == '%':  # Modulo operation (remainder after division)
        result = num1 % num2
    
    # Format the result for display
    # If the result is a whole number and not from division, show it as an integer
    # Division always returns a float (like 5.0) even for whole number results
    if result == int(result) and operation != 'div':
        return str(int(result))  # Return as integer string (e.g., "5")
    else:
        return str(result)  # Return as float string (e.g., "5.0")
if __name__ == '__main__':
    app.run(port=5555, debug=True)
