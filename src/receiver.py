from decode import *
from encode import xor

import socket

#Connection to the server
IP = "vlbelintrocrypto.hevs.ch"
PORT = 6000


def receive_msg(byte_message, decoding, decoding_value=None):
    # Transform message to table of int
    array = byte_message_to_array(byte_message)
    # With this table => encoding
    print(decoding)

    if decoding == "shift":
        if decoding_value.isnumeric():
            array = unshift(array, int(decoding_value))
        else:
            raise Exception()
    elif decoding == "xor":
        if decoding_value.isnumeric():
            array = xor(array,int(decoding_value))
        else:
            raise Exception()
    elif decoding == "vigenere":
        array = unvigenere(array, str(decoding_value))
    elif decoding == "rsa":
        if type(decoding_value) == tuple and len(decoding_value) == 2:
            array = unrsa(array, *decoding_value)
        else:
            raise Exception()
    
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

if __name__ == '__main__':
    client_socket = socket.socket()
    client_socket.connect((IP,PORT))

    #Listening the server responses
    while True:
        data = client_socket.recv(1024) # receive response
        message = receive_msg(data, 'vigenere', 'abc')
        print(message)
