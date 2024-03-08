from Decode import *
from Encode import xor

import socket
import sys

#Connection to the server
IP = "vlbelintrocrypto.hevs.ch"
PORT = 6000


def receive_msg(byte_message, decoding = ''):
    # Transform message to table of int
    array = byte_message_to_array(byte_message)
    # With this table => encoding
    if decoding == "nothing":
        print("You did nothing")
    elif decoding == "shift":
        value = int(input("Enter the shift value : "))
        array = unshift(array,value)
    elif decoding == "xor":
        value = int(input("Enter the number : "))
        array = xor(array, value)
    elif decoding == "vigenere":
        keyword = str(input("Enter the keyword : "))
        array = unvigenere(array, keyword)
    else:
        print(f"The type : {type} doesn't exist")
        sys.exit()
    
    final_message = array_to_message(array)
    return final_message

# Decode the message
def byte_message_to_array(message):
    type = chr(message[3])
    res = []

    if type == 't' or type == 's':
        message = message [6:] #remove 6first
        for i in range(0, len(message), 4):
            byte_val = message[i:i+4]
            res.append(int.from_bytes(byte_val, "big"))
        
    return res
        

def array_to_message(array) :
    new_array = []
    for i in array :
        if i >= 0:
            new_array.append(i.to_bytes((i.bit_length()+7) // 8, 'big'))
    res = ""
    for i in new_array :
        try:
            res += i.decode('utf-8')
        except:
            print('Wrong array in entry')

    return(res)

client_socket = socket.socket()
client_socket.connect((IP,PORT))

#Listening the server responses
while True:
    data = client_socket.recv(1024) # receive response
    print(data)
    message = receive_msg('data')
    print(message)
