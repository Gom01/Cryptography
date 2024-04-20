from PyQt6 import QtWidgets, uic
from pathlib import Path
from threading import Thread
from src.encode import generate_rsa_keys
from src.sender import create_msg
from src.receiver import receive_msg
from src.network import *
from src.encode import generatediffieHellmanKeys
from src.auto_task import task

class Ui(QtWidgets.QMainWindow):
    encoding_type = "No encoding"
    def __init__(self):
        self.encoding_type = "No encoding"
        self.decoding_value = ""
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(Path(__file__).parent / 'window.ui', self) # Load the .ui file
        #PushButton
        self.sendButton.clicked.connect(self.isClicked)
        self.btnTask.clicked.connect(self.task_clicked)
        self.btnTask_2.clicked.connect(self.clrMessages)
        self.clearButton.clicked.connect(self.clrwindows)
        self.generate_2.clicked.connect(self.keysGeneration)
        #RadioButton
        self.rbtnNoEncode.toggled.connect(self.choices)
        self.rbtnVigenere.toggled.connect(self.choices)
        self.rbtnShift.toggled.connect(self.choices)
        self.rbtnXor.toggled.connect(self.choices)
        self.rbtnDiffieTask.toggled.connect(self.choices_task)
        self.rbtnRSATask.toggled.connect(self.choices_task)
        #Visibility at beginning
        self.encodingValue.setVisible(False)
        self.lblEncodingValue.setVisible(False)
        #PlaceHolder
        self.messageContainer.setPlaceholderText("Waiting for a message...")
        #Threading
        self.network = Network()
        self.socket_instance = self.network.get_socket_instance()
        self.t = Thread(target=self.handle_messages).start()
        self.show()

    def closeEvent(self, event):
        self.stop = True
        event.accept()

    def handle_messages(self):
        while True:
            byte_data = self.socket_instance.recv(1024)  # receive response
            self.lstReceiveNoDecode.addItem(str(byte_data))
            if (self.commandServer.isChecked()):
                data = receive_msg(byte_data, "No encoding")
                self.lstReceive.addItem(str(data))
            else :
                data = receive_msg(byte_data, self.encoding_type, self.decoding_value)
                self.lstReceive.addItem(str(data))


    def task_clicked(self):
        if self.rbtnRSATask.isChecked():
            if self.cbxEncode.currentText() == "Encode":
                discussion = task(100, True, "rsa")
            else:
                discussion = task(100, False, "rsa")
        else:
            discussion = task(100, True, "difhel")

        for m in discussion:
            self.lstTask.addItem(m)


    def clrMessages(self):
        self.lstTask.clear()
        self.listWidget_4.clear()

    def isClicked(self):
        if (self.messageContainer.toPlainText()):
            if (self.commandServer.isChecked()):
                message_type = 's'
            else:
                message_type = 't'
            message = self.messageContainer.toPlainText()
            value = self.encodingValue.text()
            self.decoding_value = value
            self.messageContainer.clear()
            self.encodingValue.clear()
            final_message = create_msg(message, message_type, self.encoding_type, value)
            self.network.send_message(final_message)

    def clrwindows(self):
        self.messageContainer.clear()
        self.lstReceive.clear()
        self.lstReceiveNoDecode.clear()
        self.encodingValue.clear()
    def keysGeneration(self):
        type = ""
        if self.rbtnRSATask.isChecked():
            type = "rsa"

        if type == "rsa":
            self.listWidget_4.clear()
            generation = generate_rsa_keys()
            e = generation[0][1]
            n = generation[1][0]
            d = generation[1][1]
            keys = f"Public Key : (n = {n}, e = {e})\nPrivate Key : (n = {n}, d = {d})"
            self.listWidget_4.addItem(keys)

        else:
            self.listWidget_4.clear()
            generation = generatediffieHellmanKeys()
            p = str(generation[0])
            g = str(generation[1])
            keys = f"Generator value : {g}\nPrime Number : {p}"
            self.listWidget_4.addItem(keys)

    def choices_task(self):
        rb = self.sender()
        if rb.text() == "Diffie-Hellman":
            self.cbxEncode.setVisible(False)
        elif rb.text() == "RSA":
            self.cbxEncode.setVisible(True)

    #Controls parameter of RadioButton
    def choices(self):
        rb = self.sender()
        if rb.text() == "No encoding":
            self.encoding_type = "No encoding"
            self.encodingValue.setVisible(False)
            self.lblEncodingValue.setVisible(False)

        elif rb.text() == "Shift":
            self.encoding_type = "shift"
            self.encodingValue.setPlaceholderText("ENTER A NUMBER")
            self.encodingValue.setVisible(True)
            self.lblEncodingValue.setVisible(True)


        elif rb.text() == "Xor":
            self.encoding_type = "xor"
            self.encodingValue.setPlaceholderText("ENTER A NUMBER")
            self.encodingValue.setVisible(True)
            self.lblEncodingValue.setVisible(True)

        elif rb.text() == "Vigenere":
            self.encoding_type = "vigenere"
            self.encodingValue.setPlaceholderText("ENTER A KEYWORD")
            self.encodingValue.setVisible(True)
            self.lblEncodingValue.setVisible(True)



