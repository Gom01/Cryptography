import datetime

from .sender import create_msg
from .receiver import receive_msg
from .network import Network
from .encode import generate_rsa_keys
from .encode import generatediffieHellmanKeys
from .encode import pow
from datetime import datetime


def task(number_letters=6, encode=True, task_type="shift"):
    serverResponse = f"{datetime.now().strftime('%H:%M:%S')} - SERVER:  "
    clientResponse = f"{datetime.now().strftime('%H:%M:%S')} - CLIENT:    "

    network = Network()
    type_list = ["shift", "vigenere", "rsa", "difhel"]
    socket = network.get_socket_instance()
    task_type = task_type.lower()
    messages_list = []

    if task_type in type_list:
        if encode:
            if task_type == "difhel":
                message = f"task DifHel"
                messages_list.append(serverResponse+str(message))
                message = create_msg(message, "s", None)
                network.send_message(message)

                response_1 = receive_msg(socket.recv(1024), "None")
                messages_list.append(serverResponse+response_1)

                values = generatediffieHellmanKeys()
                p = values[0]
                g = values[1]

                message = f"{p},{g}"
                messages_list.append(clientResponse+str(message))
                message = create_msg(message, "s", None)
                network.send_message(message)

                response_1 = receive_msg(socket.recv(1024), "None")
                if response_1.startswith("D"):
                    response_2 = receive_msg(socket.recv(1024), "None")
                    messages_list.append(serverResponse+response_1)
                    messages_list.append(serverResponse+response_2)
                    received = int(response_2)
                    a = 12
                    sent = pow(a,g,p)
                    messages_list.append(clientResponse+ str(sent))
                    message = create_msg(str(sent), "s", None)
                    network.send_message(message)
                    response_1 = receive_msg(socket.recv(1024), "None")
                    messages_list.append(clientResponse+response_1)

                    secretShared = pow(a,received,p)
                    message = f"{secretShared}"
                    messages_list.append(clientResponse + str(message))
                    message = create_msg(message, "s", None)
                    network.send_message(message)
                    response_1 = receive_msg(socket.recv(1024), "None")
                    messages_list.append(serverResponse+response_1)


            else:
                if task_type == "rsa":
                    task_type = task_type.upper()
                message = f"task {task_type} encode {number_letters}"
                messages_list.append(clientResponse+message)
                message = create_msg(message, "s", "None")
                network.send_message(message)

                response_1 = receive_msg(socket.recv(1024), "None")
                messages_list.append(serverResponse+response_1)

                if task_type == "RSA":
                    n = response_1.split("n=")[1].split(",")[0]
                    e = response_1.split("e=")[1]
                    word = receive_msg(socket.recv(1024), "None")
                    messages_list.append(serverResponse+word)
                    encoded_message = create_msg(word, 's', task_type, (int(n), int(e)))
                else:
                    encoding_key = response_1.split(" ")[-1]
                    word = receive_msg(socket.recv(1024), "None")
                    messages_list.append(serverResponse+word)
                    encoded_message = create_msg(word, 's', task_type, encoding_key)

                messages_list.append(clientResponse+str(encoded_message))
                network.send_message(encoded_message)

                final_response = receive_msg(socket.recv(1024), "None")
                messages_list.append(serverResponse+final_response)

        ################################

        else:
            if task_type == "rsa":
                task_type = task_type.upper()
            message = f"task {task_type} decode {number_letters}"
            print(message)
            messages_list.append(clientResponse+message)
            message = create_msg(message, "s", "None")
            network.send_message(message)

            response_1 = receive_msg(socket.recv(1024), "None")
            print(response_1)
            messages_list.append(serverResponse+response_1)

            keys = generate_rsa_keys()
            n = keys[0][0]
            e = keys[0][1]
            d = keys[1][1]
            n_e_message = create_msg(f"{n},{e}", "s", None)
            print(f"{n},{e}")
            messages_list.append(clientResponse+str(n_e_message))
            network.send_message(n_e_message)

            response_2 = socket.recv(1024)
            print("Response from server")
            print(response_2)
            messages_list.append(serverResponse+str(response_2))

            decoded_message = receive_msg(response_2, "rsa", (n,d))
            print(n)
            print(d)
            print("Our decoded message")
            messages_list.append(clientResponse+str(decoded_message))
            message_decoded_send = create_msg(str(decoded_message), "s", None)
            network.send_message(message_decoded_send)
            print(message_decoded_send)


            print("Waiting for the response")
            response_3 = socket.recv(1024)
            response_3 = receive_msg(response_3,None)
            print(response_3)
            messages_list.append(serverResponse+response_3)


    return messages_list


if __name__ == "__main__":
    task(1023, False, "rsa")
