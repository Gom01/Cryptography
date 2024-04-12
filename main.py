from PyQt6 import QtWidgets

from ui.ui import Ui

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec()
