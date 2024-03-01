import socket

#Connection to the server
IP = "vlbelintrocrypto.hevs.ch"
PORT = 6000



def create_message(message, type):
    #Create a text message
    if type == 't':
        message_length : int = len(message)
        ISCt_header = bytes(f"ISCt", 'utf-8')
        total_length = message_length.to_bytes(2, byteorder='big')
        res = ISCt_header + total_length
        
        for i in range(message_length):
            res += bytes([0,0,0]) + bytes(str(message[i]), 'utf-8')
        
    return res
        
# Creation of a socket and connection to the server
client_socket = socket.socket()
client_socket.connect((IP,PORT))


message = create_message("Testing the message system.", 't')
client_socket.send(message)  # send message
data = client_socket.recv(1024) # receive response
print(data)
