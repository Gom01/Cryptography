from Decode import *

import socket

#Connection to the server
IP = "vlbelintrocrypto.hevs.ch"
PORT = 6000

# Decode the message
def message_to_array(message):
    type = chr(message[3])
    res = []

    if type == 't':
        message = message [6:] #remove 6first
        for i in range(0, len(message), 4):
            byte_val = message[i:i+4]
            res.append(int.from_bytes(byte_val, "big"))
        
    return res
        

def array_to_message(array) :
    new_Array = []
    for i in array :
        if i >= 0:
            new_Array.append(i.to_bytes((i.bit_length()+7) // 8, 'big'))
    res = ""
    for i in new_Array :
        res += i.decode('utf-8')

    return(res)




client_socket = socket.socket()
client_socket.connect((IP,PORT))

#Listening the server responses
while True:
    data = client_socket.recv(1024) # receive response
    print(data)
    message = unshift(message_to_array(data), 1000)
    decode_message = (array_to_message(message))
    print(decode_message)
