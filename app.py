import streamlit as st
import math

# Title of the app
st.title("Scientific Calculator")

# Input area for the numbers
st.write("## Enter numbers:")
num1 = st.number_input("Enter first number", format="%.10f")
num2 = st.number_input("Enter second number (optional for some operations)", format="%.10f")

# Select operation
operation = st.selectbox("Select an operation", 
                         ["Add", "Subtract", "Multiply", "Divide", 
                          "Square Root (First Number)", 
                          "Power", "Sine", "Cosine", "Tangent", 
                          "Logarithm (base 10)", "Exponential"])

# Perform calculations based on the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")

    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")

    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"Result: {num1} * {num2} = {result}")

    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {num1} / {num2} = {result}")
        else:
            st.error("Error: Cannot divide by zero")

    elif operation == "Square Root (First Number)":
        if num1 >= 0:
            result = math.sqrt(num1)
            st.success(f"Result: √{num1} = {result}")
        else:
            st.error("Error: Cannot compute square root of a negative number")

    elif operation == "Power":
        result = math.pow(num1, num2)
        st.success(f"Result: {num1} ^ {num2} = {result}")

    elif operation == "Sine":
        result = math.sin(math.radians(num1))
        st.success(f"Result: sin({num1}°) = {result}")

    elif operation == "Cosine":
        result = math.cos(math.radians(num1))
        st.success(f"Result: cos({num1}°) = {result}")

    elif operation == "Tangent":
        result = math.tan(math.radians(num1))
        st.success(f"Result: tan({num1}°) = {result}")

    elif operation == "Logarithm (base 10)":
        if num1 > 0:
            result = math.log10(num1)
            st.success(f"Result: log10({num1}) = {result}")
        else:
            st.error("Error: Logarithm undefined for non-positive numbers")

    elif operation == "Exponential":
        result = math.exp(num1)
        st.success(f"Result: exp({num1}) = {result}")
