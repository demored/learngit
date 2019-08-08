import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import firstPyQt

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = QMainWindow()
    ui = firstPyQt.Ui_MainWindow()
    ui.setupUi(myWindow)
    myWindow.show()
    sys.exit(app.exec_())