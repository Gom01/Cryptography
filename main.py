from PyQt6.QtWidgets import QApplication


from ui.ui import Ui

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Ui()
    window.setWindowTitle("Cryptography")
    app.exec()
