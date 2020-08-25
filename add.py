import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Number_addition import *

class MyFrom(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.dispsum)
        self.show()
    def dispsum(self):
        num1 = self.ui.first_line.text()
        num2 = self.ui.second_line.text()
        s=int(num1)
        t=int(num2)
        a=s+t
        self.ui.label_3.setText('Sum is :' +str(a))

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyFrom()
    w.show()
    sys.exit(app.exec_())
