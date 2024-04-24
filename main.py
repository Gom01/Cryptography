from PyQt6.QtWidgets import QApplication


from ui.ui import Ui

if __name__ == "__main__":
    import sys

    def except_hook(cls,exception,traceback):
        try:
            sys.__excepthook__(cls,exception,traceback)
        except:
            pass
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Ui()
    window.setWindowTitle("Cryptography")
    app.exec()
