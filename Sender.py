from Encode import *
from tester import sendTestEncoding
from Receiver import array_to_message, message_to_array2
import socket

# Connection to the server
IP = "vlbelintrocrypto.hevs.ch"
PORT = 6000


def create_message(arr_int, type):
    # Create a text message
    if type == 't' or type == 's':
        message_length: int = len(arr_int)
        ISCt_header = bytes(f"ISC{type}", 'utf-8')
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

message = "Salut mon ami"

encoded_message = vigenere(message_to_array(message), "Hello")

client_socket.send(sendTestEncoding("vigenere", 4))  # send message
server_m = array_to_message(message_to_array2(client_socket.recv(1024))).split()[-1]
received_m = client_socket.recv(1024)
print(vigenere(message_to_array2(received_m), server_m))
encoded_m = array_to_message(vigenere(message_to_array2(received_m), server_m))
client_socket.send(create_message(message_to_array(encoded_m), 's'))
print(array_to_message(message_to_array2(client_socket.recv(1024))))
