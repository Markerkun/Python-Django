def view_message(msg):
    message = msg[0:9] #Slice a row
    #print("message:", message)

    def private_func():
        print(message)
    return private_func #Def is closed

closure = view_message("Today is the best day!!")
closure()