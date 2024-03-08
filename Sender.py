import sys
import socket
from Encode import *

if __name__ == "__main__":
    def create_msg(message, type, encoding):
        # Transform message to table of int
        array = msg_to_array(message)
        # With this table => encoding
        if encoding == "nothing":
            print("You did nothing")
        elif encoding == "shift":
            value = int(input("Enter the shift value : "))
            array = shift(array,value)

        elif encoding == "xor":
            value = int(input("Enter the number : "))
            array = xor(array, value)

        elif encoding == "vigenere":
            keyword = str(input("Enter the keyword : "))
            array = vigenere(array, keyword)

        else:
            print(f"The type : {type} doesn't exist")
            sys.exit()

        # Convert the table to bytes
        final_message = Conversion_ArrayToByte(array, type)

        # Proceed to connect socket and send the message
        # Creation of a socket and connection to the server
        client_socket = socket.socket()
        client_socket.connect((IP, PORT))
        client_socket.send(final_message)


    # This function is used to convert the Array[Int]to bytes
    def Conversion_ArrayToByte(arr_int, type):
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


    # Connection to the server
    IP = "vlbelintrocrypto.hevs.ch"
    PORT = 6000
    create_msg("Salut mon ami, j'espère que tu vas bien !",'t',"xor")
