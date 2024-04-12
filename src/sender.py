import socket
import sys

from .encode import *


IP = "vlbelintrocrypto.hevs.ch"
PORT = 6000

def create_msg(message, message_type, encoding, encoding_value=None):
    # Transform message to table of int
    array = msg_to_array(message)
    # With this table => encoding
    if encoding == "shift":
        if encoding_value.isnumeric():
            array = shift(array, int(encoding_value))
        else:
            raise Exception()
    elif encoding == "xor":
        if encoding_value.isnumeric():
            array = xor(array,int(encoding_value))
        else:
            raise Exception()
    elif encoding == "vigenere":
        array = vigenere(array, str(encoding_value))
    elif encoding == "rsa":
        if type(encoding_value) == tuple and len(encoding_value) == 2:
            array = rsa(array, *encoding_value)
        else:
            raise Exception()

    # Convert the table to bytes
    final_message = conversion_array_to_byte(array, message_type)
    return final_message

# This function is used to convert the Array[Int]to bytes
def conversion_array_to_byte(arr_int, type):
    # Create a text message
    if type == 't' or type == 's':
        message_length: int = len(arr_int)
        ISCt_header = bytes(f"ISC{type}", 'utf-8')
        total_length = message_length.to_bytes(2, byteorder='big')
        res = ISCt_header + total_length
        for i in arr_int:
            res += i.to_bytes(4, byteorder='big')
    else:
        print(f"The type {type} doesn't exist")
        sys.exit()

    return res


# Convert the given message to an array[Int] so we can encode it
def msg_to_array(message):
    byte_arr = []
    res = []
    # string with encoding 'utf-8'
    for c in message:
        byte_arr.append(bytes(c, 'utf-8'))
    for b in byte_arr:
        res.append(int.from_bytes(b, "big"))
    return res


if __name__ == "__main__":
    # Connection to the server
    create_msg("Salut mon ami, j'espère que tu vas bien !",'t',"shift", '14')
