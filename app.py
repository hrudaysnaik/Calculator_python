from flask import Flask, render_template, request

app = Flask(__name__)

# Data structure to store history
history = []

# Core functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: return "Error: Cannot divide by zero"
    return a / b

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result_message = None
    
    # Handle incoming form submissions
    if request.method == 'POST':
        try:
            # 1. Variables & Data Types
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            
            # Variables for tracking state
            result = 0
            op_sym = ''
            
            # 2. Flow Control: If-Else for operations
            if operation == 'add':
                result = add(num1, num2)
                op_sym = '+'
            elif operation == 'subtract':
                result = subtract(num1, num2)
                op_sym = '-'
            elif operation == 'multiply':
                result = multiply(num1, num2)
                op_sym = '*'
            elif operation == 'divide':
                result = divide(num1, num2)
                op_sym = '/'
                
            # Formatting output
            if isinstance(result, str):
                result_message = result # Pass the string error message
            else:
                # Format to remove .0 if it's a clean integer for better UI
                if int(result) == result: result = int(result)
                if int(num1) == num1: num1 = int(num1)
                if int(num2) == num2: num2 = int(num2)
                
                # String formatting
                result_message = f"{num1} {op_sym} {num2} = {result}"
                
                # 3. Data Structure update
                history.append(result_message)
                
        except ValueError:
            result_message = "Error: Invalid numeric input!"

    # Render our frontend template, passing data to it
    return render_template('index.html', result=result_message, history=history)

if __name__ == '__main__':
    # Start the Flask web server
    app.run(debug=True, port=5000)
