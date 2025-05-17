def decorator_fn(func):
    def wrapper():
        print("wasay")   
        func()
        print("fahad")
    return wrapper

@decorator_fn
def hello_world():

    print("hello world")

hello_world()
