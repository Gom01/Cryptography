import threading
import time

#Sender
def sender() :
    while(True) :
        message = input("Enter message to send: ")
        print(f"Send the {message}")
        time.sleep(1)

def receiver() :
    while(True) :
        print("listening....")
        time.sleep(1)


#Creation of the threads
s = threading.Thread(target = sender)
r = threading.Thread(target = receiver)



r.start()
s.start()


r.join()
s.join()

