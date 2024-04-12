import socket


class Network:
    def __init__(self):
        IP = "vlbelintrocrypto.hevs.ch"
        PORT = 6000
        
        self.client_socket = socket.socket()
        self.client_socket.connect((IP,PORT))

    def get_socket_instance(self):
        return self.client_socket

    def send_message(self, message):
        self.client_socket.send(message)
