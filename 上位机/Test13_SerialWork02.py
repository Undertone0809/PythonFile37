# -*- coding: utf-8 -*-
# @Time    : 2021/1/9 23:13
# @Author  : Zeeland
# @File    : Test13_SerialWork02.py
# @Software: PyCharm

# Form01 implementation generated from reading ui file 'demo_1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form01(object):
    def setupUi(self, Form01):
        Form01.setObjectName("Form01")
        Form01.resize(707, 458)
        self.Form01GroupBox = QtWidgets.QGroupBox(Form01)
        self.Form01GroupBox.setGeometry(QtCore.QRect(20, 20, 167, 301))
        self.Form01GroupBox.setObjectName("Form01GroupBox")
        self.Form01Layout = QtWidgets.QFormLayout(self.Form01GroupBox)
        self.Form01Layout.setContentsMargins(10, 10, 10, 10)
        self.Form01Layout.setSpacing(10)
        self.Form01Layout.setObjectName("Form01Layout")
        self.s1__lb_1 = QtWidgets.QLabel(self.Form01GroupBox)
        self.s1__lb_1.setObjectName("s1__lb_1")
        self.Form01Layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.s1__lb_1)
        self.s1__box_1 = QtWidgets.QPushButton(self.Form01GroupBox)
        self.s1__box_1.setAutoRepeatInterval(100)
        self.s1__box_1.setDefault(True)
        self.s1__box_1.setObjectName("s1__box_1")
        self.Form01Layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.s1__box_1)
        self.s1__lb_2 = QtWidgets.QLabel(self.Form01GroupBox)
        self.s1__lb_2.setObjectName("s1__lb_2")
        self.Form01Layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.s1__lb_2)
        self.s1__box_2 = QtWidgets.QComboBox(self.Form01GroupBox)
        self.s1__box_2.setObjectName("s1__box_2")
        self.Form01Layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.s1__box_2)
        self.s1__lb_3 = QtWidgets.QLabel(self.Form01GroupBox)
        self.s1__lb_3.setObjectName("s1__lb_3")
        self.Form01Layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.s1__lb_3)
        self.s1__box_3 = QtWidgets.QComboBox(self.Form01GroupBox)
        self.s1__box_3.setObjectName("s1__box_3")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.Form01Layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.s1__box_3)
        self.s1__lb_4 = QtWidgets.QLabel(self.Form01GroupBox)
        self.s1__lb_4.setObjectName("s1__lb_4")
        self.Form01Layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.s1__lb_4)
        self.s1__box_4 = QtWidgets.QComboBox(self.Form01GroupBox)
        self.s1__box_4.setObjectName("s1__box_4")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.Form01Layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.s1__box_4)
        self.s1__lb_5 = QtWidgets.QLabel(self.Form01GroupBox)
        self.s1__lb_5.setObjectName("s1__lb_5")
        self.Form01Layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.s1__lb_5)
        self.s1__box_5 = QtWidgets.QComboBox(self.Form01GroupBox)
        self.s1__box_5.setObjectName("s1__box_5")
        self.s1__box_5.addItem("")
        self.Form01Layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.s1__box_5)
        self.open_button = QtWidgets.QPushButton(self.Form01GroupBox)
        self.open_button.setObjectName("open_button")
        self.Form01Layout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.open_button)
        self.close_button = QtWidgets.QPushButton(self.Form01GroupBox)
        self.close_button.setObjectName("close_button")
        self.Form01Layout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.close_button)
        self.s1__lb_6 = QtWidgets.QLabel(self.Form01GroupBox)
        self.s1__lb_6.setObjectName("s1__lb_6")
        self.Form01Layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.s1__lb_6)
        self.s1__box_6 = QtWidgets.QComboBox(self.Form01GroupBox)
        self.s1__box_6.setObjectName("s1__box_6")
        self.s1__box_6.addItem("")
        self.Form01Layout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.s1__box_6)
        self.state_label = QtWidgets.QLabel(self.Form01GroupBox)
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.Form01Layout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.state_label)
        self.verticalGroupBox = QtWidgets.QGroupBox(Form01)
        self.verticalGroupBox.setGeometry(QtCore.QRect(210, 20, 401, 241))
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.s2__receive_text = QtWidgets.QTextBrowser(self.verticalGroupBox)
        self.s2__receive_text.setObjectName("s2__receive_text")
        self.verticalLayout.addWidget(self.s2__receive_text)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(Form01)
        self.verticalGroupBox_2.setGeometry(QtCore.QRect(210, 280, 401, 101))
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.s3__send_text = QtWidgets.QTextEdit(self.verticalGroupBox_2)
        self.s3__send_text.setObjectName("s3__send_text")
        self.verticalLayout_2.addWidget(self.s3__send_text)
        self.s3__send_button = QtWidgets.QPushButton(Form01)
        self.s3__send_button.setGeometry(QtCore.QRect(620, 310, 61, 31))
        self.s3__send_button.setObjectName("s3__send_button")
        self.s3__clear_button = QtWidgets.QPushButton(Form01)
        self.s3__clear_button.setGeometry(QtCore.QRect(620, 350, 61, 31))
        self.s3__clear_button.setObjectName("s3__clear_button")
        self.Form01GroupBox1 = QtWidgets.QGroupBox(Form01)
        self.Form01GroupBox1.setGeometry(QtCore.QRect(20, 340, 171, 101))
        self.Form01GroupBox1.setObjectName("Form01GroupBox1")
        self.Form01Layout_2 = QtWidgets.QFormLayout(self.Form01GroupBox1)
        self.Form01Layout_2.setContentsMargins(10, 10, 10, 10)
        self.Form01Layout_2.setSpacing(10)
        self.Form01Layout_2.setObjectName("Form01Layout_2")
        self.label = QtWidgets.QLabel(self.Form01GroupBox1)
        self.label.setObjectName("label")
        self.Form01Layout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.Form01GroupBox1)
        self.label_2.setObjectName("label_2")
        self.Form01Layout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.Form01GroupBox1)
        self.lineEdit.setObjectName("lineEdit")
        self.Form01Layout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Form01GroupBox1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.Form01Layout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.hex_send = QtWidgets.QCheckBox(Form01)
        self.hex_send.setGeometry(QtCore.QRect(620, 280, 71, 16))
        self.hex_send.setObjectName("hex_send")
        self.hex_receive = QtWidgets.QCheckBox(Form01)
        self.hex_receive.setGeometry(QtCore.QRect(620, 40, 71, 16))
        self.hex_receive.setObjectName("hex_receive")
        self.s2__clear_button = QtWidgets.QPushButton(Form01)
        self.s2__clear_button.setGeometry(QtCore.QRect(620, 80, 61, 31))
        self.s2__clear_button.setObjectName("s2__clear_button")
        self.timer_send_cb = QtWidgets.QCheckBox(Form01)
        self.timer_send_cb.setGeometry(QtCore.QRect(260, 390, 71, 16))
        self.timer_send_cb.setObjectName("timer_send_cb")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form01)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 390, 61, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.dw = QtWidgets.QLabel(Form01)
        self.dw.setGeometry(QtCore.QRect(420, 390, 54, 20))
        self.dw.setObjectName("dw")
        self.verticalGroupBox.raise_()
        self.verticalGroupBox_2.raise_()
        self.Form01GroupBox.raise_()
        self.s3__send_button.raise_()
        self.s3__clear_button.raise_()
        self.Form01GroupBox.raise_()
        self.hex_send.raise_()
        self.hex_receive.raise_()
        self.s2__clear_button.raise_()
        self.timer_send_cb.raise_()
        self.lineEdit_3.raise_()
        self.dw.raise_()

        self.retranslateUi(Form01)
        QtCore.QMetaObject.connectSlotsByName(Form01)

    def retranslateUi(self, Form01):
        _translate = QtCore.QCoreApplication.translate
        Form01.setWindowTitle(_translate("Form01", "Form01"))
        self.Form01GroupBox.setTitle(_translate("Form01", "串口设置"))
        self.s1__lb_1.setText(_translate("Form01", "串口检测："))
        self.s1__box_1.setText(_translate("Form01", "检测串口"))
        self.s1__lb_2.setText(_translate("Form01", "串口选择："))
        self.s1__lb_3.setText(_translate("Form01", "波特率："))
        self.s1__box_3.setItemText(0, _translate("Form01", "115200"))
        self.s1__box_3.setItemText(1, _translate("Form01", "2400"))
        self.s1__box_3.setItemText(2, _translate("Form01", "4800"))
        self.s1__box_3.setItemText(3, _translate("Form01", "9600"))
        self.s1__box_3.setItemText(4, _translate("Form01", "14400"))
        self.s1__box_3.setItemText(5, _translate("Form01", "19200"))
        self.s1__box_3.setItemText(6, _translate("Form01", "38400"))
        self.s1__box_3.setItemText(7, _translate("Form01", "57600"))
        self.s1__box_3.setItemText(8, _translate("Form01", "76800"))
        self.s1__box_3.setItemText(9, _translate("Form01", "12800"))
        self.s1__box_3.setItemText(10, _translate("Form01", "230400"))
        self.s1__box_3.setItemText(11, _translate("Form01", "460800"))
        self.s1__lb_4.setText(_translate("Form01", "数据位："))
        self.s1__box_4.setItemText(0, _translate("Form01", "8"))
        self.s1__box_4.setItemText(1, _translate("Form01", "7"))
        self.s1__box_4.setItemText(2, _translate("Form01", "6"))
        self.s1__box_4.setItemText(3, _translate("Form01", "5"))
        self.s1__lb_5.setText(_translate("Form01", "校验位："))
        self.s1__box_5.setItemText(0, _translate("Form01", "N"))
        self.open_button.setText(_translate("Form01", "打开串口"))
        self.close_button.setText(_translate("Form01", "关闭串口"))
        self.s1__lb_6.setText(_translate("Form01", "停止位："))
        self.s1__box_6.setItemText(0, _translate("Form01", "1"))
        self.verticalGroupBox.setTitle(_translate("Form01", "接受区"))
        self.verticalGroupBox_2.setTitle(_translate("Form01", "发送区"))
        self.s3__send_text.setHtml(_translate("Form01", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">123456</p></body></html>"))

        #发送按键s3__send_button
        self.s3__send_button.setText(_translate("Form01", "发送"))
        self.s3__clear_button.setText(_translate("Form01", "清除"))
        self.Form01GroupBox1.setTitle(_translate("Form01", "串口状态"))
        self.label.setText(_translate("Form01", "已接收："))
        self.label_2.setText(_translate("Form01", "已发送："))
        self.hex_send.setText(_translate("Form01", "Hex发送"))
        self.hex_receive.setText(_translate("Form01", "Hex接收"))
        self.s2__clear_button.setText(_translate("Form01", "清除"))
        self.timer_send_cb.setText(_translate("Form01", "定时发送"))
        self.lineEdit_3.setText(_translate("Form01", "1000"))
        self.dw.setText(_translate("Form01", "ms/次"))

import sys
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer


class Pyqt5_Serial(QtWidgets.QWidget, Ui_Form01):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("串口小助手")
        self.ser = serial.Serial()
        self.port_check()

        # 接收数据和发送数据数目置零
        #记录接受的数据数
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))

        #记录发送的数据数
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))

    def init(self):
        # 串口检测按钮
        self.s1__box_1.clicked.connect(self.port_check)

        # 串口信息显示
        self.s1__box_2.currentTextChanged.connect(self.port_imf)

        # 打开串口按钮
        self.open_button.clicked.connect(self.port_open)

        # 关闭串口按钮
        self.close_button.clicked.connect(self.port_close)

        # 发送数据按钮
        self.s3__send_button.clicked.connect(self.data_send)

        # 定时发送数据
        self.timer_send = QTimer()
        self.timer_send.timeout.connect(self.data_send)
        self.timer_send_cb.stateChanged.connect(self.data_send_timer)

        # 定时器接收数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)

        # 清除发送窗口
        self.s3__clear_button.clicked.connect(self.send_data_clear)

        # 清除接收窗口
        self.s2__clear_button.clicked.connect(self.receive_data_clear)

    # 串口检测
    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.s1__box_2.clear()
        for port in port_list:
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]
            self.s1__box_2.addItem(port[0])
        if len(self.Com_Dict) == 0:
            self.state_label.setText(" 无串口")

    # 串口信息
    def port_imf(self):
        # 显示选定的串口的详细信息
        imf_s = self.s1__box_2.currentText()
        if imf_s != "":
            self.state_label.setText(self.Com_Dict[self.s1__box_2.currentText()])

    # 打开串口
    def port_open(self):
        self.ser.port = self.s1__box_2.currentText()
        self.ser.baudrate = int(self.s1__box_3.currentText())
        self.ser.bytesize = int(self.s1__box_4.currentText())
        self.ser.stopbits = int(self.s1__box_6.currentText())
        self.ser.parity = self.s1__box_5.currentText()

        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None

        # 打开串口接收定时器，周期为2ms
        self.timer.start(2)

        if self.ser.isOpen():
            self.open_button.setEnabled(False)
            self.close_button.setEnabled(True)
            self.Form01GroupBox1.setTitle("串口状态（已开启）")

    # 关闭串口
    def port_close(self):
        self.timer.stop()
        self.timer_send.stop()
        try:
            self.ser.close()
        except:
            pass
        self.open_button.setEnabled(True)
        self.close_button.setEnabled(False)
        self.lineEdit_3.setEnabled(True)
        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))
        self.Form01GroupBox1.setTitle("串口状态（已关闭）")

    # 发送数据
    #输入16进制的数据
    #发送16进制数据给传感器
    def data_send(self):
        if self.ser.isOpen():

            #接受输入的数据
            #s3__send_text是输入数据文本框
            input_s = self.s3__send_text.toPlainText()

            #如果不是空字符串
            if input_s != "":

                #判断是否勾选了16进制发送框
                if self.hex_send.isChecked():

                    #去除字符串两边的空格
                    input_s = input_s.strip()

                    #创建一个空数组
                    send_list = []

                    #再次确认数据存在
                    while input_s != '':
                        try:

                            #输入16进制的数字
                            num = int(input_s[0:2], 16)
                        except ValueError:

                            #如果不是16进制则报错
                            QMessageBox.critical(self, 'wrong data', '请输入十六进制数据，以空格分开!')
                            return None

                        #去除空格
                        input_s = input_s[2:].strip()
                        send_list.append(num)

                    input_s = bytes(send_list)
                else:
                    # 如果不是16进制，则以ascii码发送
                    input_s = (input_s + '\r\n').encode('utf-8')

                #输出对应数据流到传感器
                num = self.ser.write(input_s)

                self.data_num_sended += num
                self.lineEdit_2.setText(str(self.data_num_sended))
        else:
            pass

    # 接收数据
    # bytes数据流转换为字符串输出
    # 需要了解这个方法转换出的数据类型
    # 推断：输出字符串
    #从read方法中读取数据
    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            #关闭端口
            self.port_close()
            return None

        #如果接受到数据
        if num > 0:
            data = self.ser.read(num)
            num = len(data)
            # hex显示
            if self.hex_receive.checkState():
                out_s = ''
                for i in range(0, len(data)):
                    out_s = out_s + '{:02X}'.Form01at(data[i]) + ' '
                self.s2__receive_text.insertPlainText(out_s)
            else:
                # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
                self.s2__receive_text.insertPlainText(data.decode('utf-8'))

            # 统计接收字符的数量
            self.data_num_received += num
            self.lineEdit.setText(str(self.data_num_received))

            #全选
            # 获取到text光标
            textCursor = self.s2__receive_text.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            self.s2__receive_text.setTextCursor(textCursor)
        else:
            pass

    # 定时发送数据
    def data_send_timer(self):
        #判断是否选择了定式发送功能
        if self.timer_send_cb.isChecked():

            #定式发送的秒数
            self.timer_send.start(int(self.lineEdit_3.text()))
            #设置文本框是否可编辑
            #不可用后变暗
            self.lineEdit_3.setEnabled(False)
        else:
            #关闭之后
            #文本框可编辑
            self.timer_send.stop()
            self.lineEdit_3.setEnabled(True)

    # 清除显示
    def send_data_clear(self):
        self.s3__send_text.setText("")

    def receive_data_clear(self):
        self.s2__receive_text.setText("")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5_Serial()
    myshow.show()
    sys.exit(app.exec_())