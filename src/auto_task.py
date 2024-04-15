from .sender import create_msg
from .receiver import receive_msg
from .network import Network


def shift_tasks(number_letters = 6, encode=True):
    network = Network()
    socket = network.get_socket_instance()

    if(encode):
        message = f"task shift encode {number_letters}"
        message = create_msg(message, "s", "None")
        network.send_message(message)
        
        shift_number = receive_msg(socket.recv(1024), "None").split(" ")[-1]
        word = receive_msg(socket.recv(1024), "None")
        encoded_message = create_msg(word, 's', "shift", shift_number)
        network.send_message(encoded_message)
        print(receive_msg(socket.recv(1024), "None"))



if __name__ == "__main__":
    shift_tasks()
