# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(829, 514)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_receive = QtWidgets.QTextBrowser(Form)
        self.textBrowser_receive.setObjectName("textBrowser_receive")
        self.verticalLayout.addWidget(self.textBrowser_receive)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser_modify = QtWidgets.QTextBrowser(Form)
        self.textBrowser_modify.setObjectName("textBrowser_modify")
        self.verticalLayout_2.addWidget(self.textBrowser_modify)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_openFile = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_openFile.sizePolicy().hasHeightForWidth())
        self.btn_openFile.setSizePolicy(sizePolicy)
        self.btn_openFile.setObjectName("btn_openFile")
        self.horizontalLayout_2.addWidget(self.btn_openFile)
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.fontComboBox_selectFormat = QtWidgets.QFontComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontComboBox_selectFormat.sizePolicy().hasHeightForWidth())
        self.fontComboBox_selectFormat.setSizePolicy(sizePolicy)
        self.fontComboBox_selectFormat.setObjectName("fontComboBox_selectFormat")
        self.horizontalLayout_2.addWidget(self.fontComboBox_selectFormat)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_first = QtWidgets.QLineEdit(Form)
        self.lineEdit_first.setObjectName("lineEdit_first")
        self.horizontalLayout_3.addWidget(self.lineEdit_first)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_second = QtWidgets.QLineEdit(Form)
        self.lineEdit_second.setObjectName("lineEdit_second")
        self.horizontalLayout_3.addWidget(self.lineEdit_second)
        self.pushButton_transform = QtWidgets.QPushButton(Form)
        self.pushButton_transform.setObjectName("pushButton_transform")
        self.horizontalLayout_3.addWidget(self.pushButton_transform)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser_receive.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("Form", "转换前"))
        self.label_6.setText(_translate("Form", "转换后"))
        self.label.setText(_translate("Form", "                              提示:将所有文件放在同一个文件夹中"))
        self.btn_openFile.setText(_translate("Form", "打开文件"))
        self.label_2.setText(_translate("Form", "           文件后缀："))
        self.label_3.setText(_translate("Form", "修改名称:"))
        self.lineEdit_first.setText(_translate("Form", "这是第"))
        self.label_4.setText(_translate("Form", "i"))
        self.lineEdit_second.setText(_translate("Form", "个文件"))
        self.pushButton_transform.setText(_translate("Form", "开始转换"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())