# from PyQt5 import QtWidgets
from vkonline import *
import sys


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    # application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
