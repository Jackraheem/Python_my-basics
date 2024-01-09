#In Python, decorators are a powerful and flexible way to modify or enhance the behavior of functions or methods without changing their code. Decorators are essentially functions that take another function as an argument and return a new function, typically extending or modifying the behavior of the original function. They are widely used in Python for tasks like logging, authentication, access control, and more.

#Decorators are applied to functions or methods using the "@" symbol followed by the decorator name, placed above the function definition. Here's a basic structure of a decorator:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

