import streamlit as st
import math

# Function to perform basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to perform scientific operations
def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x, base):
    return math.log(x, base)

# Streamlit app
st.title("Scientific Calculator")

# Choose the type of operation
operation = st.selectbox("Select operation", [
    "Add", "Subtract", "Multiply", "Divide", 
    "Power", "Square Root", "Sine", "Cosine", "Tangent", "Logarithm"
])

# Input based on the operation
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num1 = st.number_input("Enter first number", step=1.0)
    num2 = st.number_input("Enter second number", step=1.0)
    
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
     
