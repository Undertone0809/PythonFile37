# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test01.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 542)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 140, 261, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(200, 270, 261, 131))
        self.textEdit.setObjectName("textEdit")

        self.pushButton.clicked.connect(Form.something)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "this is a test"))
        self.pushButton.setText(_translate("Form", "PushButton"))


#在这个类中编辑定义需要重写的底层代码
class Test_Work(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        #继承父类的方法
        super().__init__()
        #用父类的UI内容填装自身的空盘子（空的QWidget）
        self.setupUi(self)


    def something(self):
        print("the button is here")
        self.textEdit.append("这个button被执行了")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = Test_Work()
    Form.show()
    sys.exit(app.exec_())