from Encode import *

import socket

# Connection to the server
IP = "vlbelintrocrypto.hevs.ch"
PORT = 6000


def create_message(arr_int, type):
    # Create a text message
    if type == 't':
        message_length: int = len(arr_int)
        ISCt_header = bytes(f"ISCt", 'utf-8')
        total_length = message_length.to_bytes(2, byteorder='big')
        res = ISCt_header + total_length

        for i in arr_int:
            res += i.to_bytes(4, byteorder='big')
    return res


def message_to_array(message):
    byte_arr = []
    res = []

    # string with encoding 'utf-8'
    for c in message:
        byte_arr.append(bytes(c, 'utf-8'))

    for b in byte_arr:
        res.append(int.from_bytes(b, "big"))

    return res


# Creation of a socket and connection to the server
client_socket = socket.socket()
client_socket.connect((IP, PORT))

message = "Testing the message system."

encoded_message = shift(message_to_array(message), 1000)
client_socket.send(create_message(encoded_message, 't'))  # send message
