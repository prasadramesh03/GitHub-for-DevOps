"""
This is the demo module for testing purposes.
"""


# Function to demonstrate the issue
def demo_function():
    """
    This function demonstrates the issues mentioned in the pylint output.
    """
    a = 5  # A variable used for demonstration
    b = 10  # Another variable used for demonstration
    d = a + b  # Correctly defined the variable 'd'

    return d


result = demo_function()
print(result)
