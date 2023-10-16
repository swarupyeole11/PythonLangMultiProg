import logging

# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function
def log_function_call(func):
    def decorated(*args, **kwargs):
        print(logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}"))
        result = func(*args, **kwargs)
        print(logging.info(f"{func.__name__} returned {result}"))
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

print(my_function(2,3))
