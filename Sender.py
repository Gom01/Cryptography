import socket

#Connection to the server
IP = "vlbelintrocrypto.hevs.ch"
PORT = 6000

def create_message(message, type):
    if type == 't':
        message_length = len(message)
        header = bytes(f"ISCt", 'utf-8')
        length = message_length.to_bytes(2, byteorder='big')
        res = header + length
        
        for i in range(message_length):
            res += bytes([0,0,0]) + bytes(str(message[i]), 'utf-8')
        
    return res
        


client_socket = socket.socket()
client_socket.connect((IP,PORT))

message = create_message("Bonjour, test 1212", 't')
client_socket.send(message)  # send message
data = client_socket.recv(1024) # receive response
print(data)
