# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtWidgets, uic
from pathlib import Path


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(Path(__file__).parent / 'window.ui', self) # Load the .ui file
        self.sendButton.clicked.connect(self.isClicked)
        self.encodingValue.setVisible(False) #Visibility of encodingValue
        self.lblEncodingValue.setVisible(False)

        self.rbtnNoEncode.toggled.connect(self.is_Checked)
        self.rbtnVigenere.toggled.connect(self.is_Checked)
        self.rbtnRSA.toggled.connect(self.is_Checked)
        self.rbtnShift.toggled.connect(self.is_Checked)
        self.show()  # Show the GUI

    def isClicked(self):
        message = self.messageContainer.toPlainText()
        value = self.encodingValue.text()
        print(f"Message : {message} Endoding value : {value}")
        self.messageContainer.clear()
        self.encodingValue.clear()

    def is_Checked(self):
        rb = self.sender()
        if rb.isChecked():
            if rb.text() == "No encoding":
                self.encodingValue.setVisible(False)
                self.lblEncodingValue.setVisible(False)
            else:
                self.encodingValue.setVisible(True)
                self.lblEncodingValue.setVisible(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec()
