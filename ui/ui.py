from PyQt6 import QtWidgets, uic
from pathlib import Path
import numpy as np
from threading import Thread
from src.encode import generate_rsa_keys
from src.sender import create_msg
from src.receiver import receive_msg
from src.network import *
from src.encode import generatediffieHellmanKeys
class Ui(QtWidgets.QMainWindow):
    encoding_type = "No encoding"
    def __init__(self):
        self.encoding_type = "No encoding"
        self.decoding_value = ""
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(Path(__file__).parent / 'window.ui', self) # Load the .ui file
        #PushButton
        self.sendButton.clicked.connect(self.isClicked)
        self.clearButton.clicked.connect(self.clrwindows)
        self.generate.clicked.connect(self.keysGeneration)
        #RadioButton
        self.rbtnNoEncode.toggled.connect(self.choices)
        self.rbtnVigenere.toggled.connect(self.choices)
        self.rbtnRSA.toggled.connect(self.choices)
        self.rbtnDiffie.toggled.connect(self.choices)
        self.rbtnShift.toggled.connect(self.choices)
        self.rbtnXor.toggled.connect(self.choices)
        #Visibility at beginning
        self.encodingValue.setVisible(False)
        self.lblEncodingValue.setVisible(False)
        self.generate.setVisible(False)
        self.listWidget.setVisible(False)
        self.dha.setVisible(False)
        self.dhb.setVisible(False)
        self.dhabvalue.setVisible(False)
        #PlaceHolder
        self.messageContainer.setPlaceholderText("Waiting for a message...")

        #Threading
        self.network = Network()
        self.socket_instance = self.network.get_socket_instance()
        Thread(target=self.handle_messages).start()
        self.show()



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
            if self.rbtnRSA.isChecked():
                n = np.int64(self.dha.text())
                e = np.int64(self.dhb.text())
                value = (n,e)
                final_message = create_msg(message, message_type, self.encoding_type, value)
            else:
                final_message = create_msg(message, message_type, self.encoding_type, value)
            self.network.send_message(final_message)

    def clrwindows(self):
        self.messageContainer.clear()
        self.lstReceive.clear()
        self.lstReceiveNoDecode.clear()
        self.listWidget.clear()
        self.dha.clear()
        self.dhb.clear()
    def keysGeneration(self):
        self.listWidget.clear()
        type = ""
        if self.rbtnRSA.isChecked():
            type = "rsa"
        elif self.rbtnDiffie.isChecked():
            type = "df"

        if type == "rsa":
            generation = generate_rsa_keys()
            n1 = generation[0][0]
            e = generation[0][1]
            n2 = generation[1][0]
            d = generation[1][1]
            keys = f"[({n1}, {e}), ({n2}, {d})]"
            self.listWidget.addItem(str(keys))
        if type == "df":
            threeValues = generatediffieHellmanKeys()
            n = threeValues[0]
            p = threeValues[1]
            g = threeValues[2]
            self.listWidget.addItem(str(f"n : {n}, p : {p}, g : {g}"))

    #Controls parameter of RadioButton
    def choices(self):
        rb = self.sender()
        if rb.text() == "No encoding":
            self.encoding_type = "No encoding"
            self.encodingValue.setVisible(False)
            self.lblEncodingValue.setVisible(False)
            self.generate.setVisible(False)
            self.listWidget.setVisible(False)
            self.dha.setVisible(False)
            self.dhb.setVisible(False)
            self.dhabvalue.setVisible(False)

        elif rb.text() == "Shift":
            self.encoding_type = "shift"
            self.encodingValue.setPlaceholderText("ENTER A NUMBER")
            self.encodingValue.setVisible(True)
            self.lblEncodingValue.setVisible(True)
            self.generate.setVisible(False)
            self.listWidget.setVisible(False)
            self.dha.setVisible(False)
            self.dhb.setVisible(False)
            self.dhabvalue.setVisible(False)
        elif rb.text() == "Xor":
            self.encoding_type = "xor"
            self.encodingValue.setPlaceholderText("ENTER A NUMBER")
            self.encodingValue.setVisible(True)
            self.lblEncodingValue.setVisible(True)
            self.generate.setVisible(False)
            self.listWidget.setVisible(False)
            self.dha.setVisible(False)
            self.dhb.setVisible(False)
            self.dhabvalue.setVisible(False)
        elif rb.text() == "Vigenere":
            self.encoding_type = "vigenere"
            self.encodingValue.setPlaceholderText("ENTER A KEYWORD")
            self.encodingValue.setVisible(True)
            self.lblEncodingValue.setVisible(True)
            self.generate.setVisible(False)
            self.listWidget.setVisible(False)
            self.dha.setVisible(False)
            self.dhb.setVisible(False)
            self.dhabvalue.setVisible(False)
        elif rb.text() == "RSA":
            self.encoding_type = "rsa"
            self.encodingValue.setVisible(False)
            self.lblEncodingValue.setVisible(False)
            self.generate.setVisible(True)
            self.listWidget.setVisible(True)
            self.dha.setVisible(True)
            self.dhb.setVisible(True)
            self.dhabvalue.setVisible(True)
            self.dha.setPlaceholderText("N")
            self.dhb.setPlaceholderText("E")
        elif rb.text() == "Diffie-Hellmann":
            self.encoding_type = "diffie-hellman"
            self.encodingValue.setVisible(False)
            self.lblEncodingValue.setVisible(False)
            self.generate.setVisible(True)
            self.listWidget.setVisible(True)
            self.dha.setVisible(True)
            self.dhb.setVisible(True)
            self.dhabvalue.setVisible(True)
            self.dha.setPlaceholderText("G")
            self.dhb.setPlaceholderText("P")