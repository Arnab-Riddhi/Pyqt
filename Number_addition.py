# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Number_addition.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Addition by ARNAB")
        Dialog.resize(746, 559)
        self.first_line = QtWidgets.QLineEdit(Dialog)
        self.first_line.setGeometry(QtCore.QRect(420, 80, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.first_line.setFont(font)
        self.first_line.setObjectName("first_line")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 80, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 160, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.second_line = QtWidgets.QLineEdit(Dialog)
        self.second_line.setGeometry(QtCore.QRect(420, 160, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.second_line.setFont(font)
        self.second_line.setObjectName("second_line")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 260, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 360, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Addition by ARNAB"))
        self.label.setText(_translate("Dialog", "Enter First number :"))
        self.label_2.setText(_translate("Dialog", "Enter Second number :"))
        self.pushButton.setText(_translate("Dialog", "Add"))
        self.label_3.setText(_translate("Dialog", "Enter First number :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
