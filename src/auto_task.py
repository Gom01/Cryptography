from .sender import create_msg
from .receiver import receive_msg
from .network import Network
from .encode import generate_rsa_keys
from .encode import generatediffieHellmanKeys
from .encode import pow


def task(number_letters=6, encode=True, task_type="shift"):
    network = Network()
    type_list = ["shift", "vigenere", "rsa", "difhel"]
    socket = network.get_socket_instance()
    task_type = task_type.lower()
    messages_list = []

    if task_type in type_list:
        if encode:
            if task_type == "difhel":
                message = f"task DifHel"
                message = create_msg(message, "s", None)
                network.send_message(message)
                messages_list.append("you : " + str(message))

                response_1 = receive_msg(socket.recv(1024), "None")
                messages_list.append("server : " + response_1)

                values = generatediffieHellmanKeys()
                p = values[0]
                g = values[1]

                message = f"{p},{g}"
                message = create_msg(message, "s", None)
                network.send_message(message)
                messages_list.append("you : " + str(message))

                response_1 = receive_msg(socket.recv(1024), "None")
                if response_1.startswith("D"):
                    response_2 = receive_msg(socket.recv(1024), "None")
                    messages_list.append("server : " + response_1)
                    messages_list.append("server : " + response_2)
                    received = int(response_2)
                    a = 12
                    sent = pow(a,g,p)
                    message = create_msg(str(sent), "s", None)
                    network.send_message(message)
                    messages_list.append("you : " + str(message))
                    response_1 = receive_msg(socket.recv(1024), "None")
                    messages_list.append("server : " + response_1)

                    secretShared = pow(a,received,p)
                    message = f"{secretShared}"
                    message = create_msg(message, "s", None)
                    network.send_message(message)
                    messages_list.append("you : " + str(message))
                    response_1 = receive_msg(socket.recv(1024), "None")
                    messages_list.append("server : " + response_1)







            else:
                if task_type == "rsa":
                    task_type = task_type.upper()
                message = f"task {task_type} encode {number_letters}"
                messages_list.append("you : " + message)
                message = create_msg(message, "s", "None")
                network.send_message(message)

                response_1 = receive_msg(socket.recv(1024), "None")
                messages_list.append("server : " + response_1)

                if task_type == "RSA":
                    n = response_1.split("n=")[1].split(",")[0]
                    e = response_1.split("e=")[1]
                    word = receive_msg(socket.recv(1024), "None")
                    messages_list.append("server : " + word)
                    encoded_message = create_msg(word, 's', task_type, (int(n), int(e)))
                else:
                    encoding_key = response_1.split(" ")[-1]
                    word = receive_msg(socket.recv(1024), "None")
                    messages_list.append("server : " + word)
                    encoded_message = create_msg(word, 's', task_type, encoding_key)

                messages_list.append("you : " + str(encoded_message))
                network.send_message(encoded_message)

                final_response = receive_msg(socket.recv(1024), "None")
                messages_list.append("server : " + final_response)
        else:
            if task_type == "rsa":
                task_type = task_type.upper()
            message = f"task {task_type} decode {number_letters}"
            messages_list.append("you : " + message)
            message = create_msg(message, "s", "None")
            network.send_message(message)

            response_1 = receive_msg(socket.recv(1024), "None")
            messages_list.append("server : " + response_1)
            keys = generate_rsa_keys()
            n = keys[0][0]
            e = keys[0][1]
            d = keys[1][1]

            n_e_message = create_msg(f"{n},{e}", "s", None, None)
            messages_list.append("you : " + str(n_e_message))
            network.send_message(n_e_message)

            response_2 = socket.recv(1024)
            messages_list.append("server : " + str(response_2))
            decoded_message = receive_msg(response_2, "rsa", (n,d))
            messages_list.append("you : " + decoded_message)
            message_decoded_send = create_msg(decoded_message, "s", "None")
            network.send_message(message_decoded_send)
            messages_list.append("server : " + receive_msg(socket.recv(1024), "None"))
    
    return messages_list


if __name__ == "__main__":
    task(6, True, "difhel")
