def decorator(func):
    def private_decorator():
        print("----Start----")
        func()
        print("-----End-----")
    return private_decorator

@decorator
def hello_message():
    print("Hello!!")

hello_message()