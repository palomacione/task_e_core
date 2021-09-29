from window import Ui_MainWindow
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication
import sys

def main():
    app_ui = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app_ui.exec_())

main()