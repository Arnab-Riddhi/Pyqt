import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from Number_addition import *

class MyFrom(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.dispsum)
        self.ui.label_3.setText("")  # set text to blank when starting the app # fix issue : irrelevant label
        self.show()
    def dispsum(self):
        num1 = self.ui.first_line.text()
        num2 = self.ui.second_line.text()

        if self.checkEntrytype(num1) == self.checkEntrytype(num2) == 'valid':
            s=float(num1)
            t=float(num2)
            a=s+t
            self.ui.label_3.setText('Sum is :' +str(a))
        else:
            if '' in [num1, num2]:
                message = QMessageBox(QMessageBox.Critical, "Wrong/Invalid Input", "please fill all the field before pressing \"Add\" button",QMessageBox.Retry)
            else:
                message = QMessageBox(QMessageBox.Critical, "Wrong/Invalid Input", "Invalid Input, allowed inputs are:\nFloat and Integer type",QMessageBox.Retry)
            message.exec_()
            self.ui.first_line.setFocus()

    def checkEntrytype(self, num):
        try:
            if num.isdigit():
                return 'valid'
            elif str(float(num)) == num:  # value error will rise from here
                return 'valid'
            else:
                return 'str'
        except ValueError:
            return 'str'
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyFrom()
    w.show()
    sys.exit(app.exec_())
