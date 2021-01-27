
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_Version01(object):
    def __init__(self):
        super().__init__()
        self.ser =serial.Serial()


    def setupUi(self, Version01):
        Version01.setObjectName("Version01")
        Version01.resize(1000, 700)

        #连接按钮
        self.LianJie = QtWidgets.QPushButton(Version01)
        self.LianJie.setGeometry(QtCore.QRect(180, 510, 150, 50))
        self.LianJie.setObjectName("LianJie")

        #接受文本框
        self.JieShouText = QtWidgets.QTextBrowser(Version01)
        self.JieShouText.setGeometry(QtCore.QRect(610, 300, 291, 251))
        self.JieShouText.setObjectName("JieShouText")

        #输入文本框
        self.ShuRuText = QtWidgets.QTextEdit(Version01)
        self.ShuRuText.setGeometry(QtCore.QRect(90, 400, 361, 87))
        self.ShuRuText.setObjectName("ShuRuText")


        self.label = QtWidgets.QLabel(Version01)
        self.label.setGeometry(QtCore.QRect(620, 244, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Version01)
        self.label_2.setGeometry(QtCore.QRect(90, 330, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Version01)
        self.pushButton.setGeometry(QtCore.QRect(60, 100, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Version01)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 160, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(Version01)
        self.textBrowser.setGeometry(QtCore.QRect(220, 100, 181, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(Version01)
        self.label_3.setGeometry(QtCore.QRect(230, 70, 101, 21))
        self.label_3.setObjectName("label_3")

        #将click行为作为一个信号
        #发送数据
        self.LianJie.clicked.connect(self.data_send)
        # self.LianJie.clicked.connect(self.data_receive())

        self.pushButton.clicked.connect(self.connect)

        self.retranslateUi(Version01)
        QtCore.QMetaObject.connectSlotsByName(Version01)

    def retranslateUi(self, Version01):
        _translate = QtCore.QCoreApplication.translate
        Version01.setWindowTitle(_translate("Version01", "Form"))
        self.LianJie.setText(_translate("Version01", "发送"))
        self.label.setText(_translate("Version01", "接受区"))
        self.label_2.setText(_translate("Version01", "输入区"))
        self.pushButton.setText(_translate("Version01", "端口连接"))
        self.pushButton_2.setText(_translate("Version01", "端口断开"))
        self.label_3.setText(_translate("Version01", "连接状态"))

    def connect(self):
        try:
            # 传入参数
            ser = serial.Serial("COM1", 115200, timeout=0.01)
            self.textBrowser.append('连接成功')
        except Exception as e:
            print('端口连接失败,错误原因：\n', e)
            self.textBrowser.append('端口连接失败')

    def hexShow(argv):
        try:
            result = ''
            hLen = len(argv)
            for i in range(hLen):
                hvol = argv[i]

                # 不足两位，则补0,以16进制表示bytes数据流
                hhex = '%02x' % hvol
                result += hhex + ' '
            return result
        except Exception as e:
            print("---异常---：", e)

        # 发送数据
        # 输入16进制的数据
        # 发送16进制数据给传感器

    def data_send(self):
        print("数据即将被发送")
        # 接受输入的数据
        # s3__send_text是输入数据文本框
        input_s = self.ShuRuText.toPlainText()

        # 如果不是空字符串
        if input_s != "":

            # 判断是否勾选了16进制发送框
            # 去除字符串两边的空格
            input_s = input_s.strip()

            # 创建一个空数组
            send_list = []

            # 再次确认数据存在
            while input_s != '':
                try:

                    # 输入16进制的数字
                    num = int(input_s[0:2], 16)
                except ValueError:

                    return None
                # 去除空格
                input_s = input_s[2:].strip()
                send_list.append(num)

                self.ser
                # 输出对应数据流到传感器
                num = self.ser.write(input_s)

            input_s = bytes(send_list)
            print("数据被发送了")



    # 接收数据
    # bytes数据流转换为字符串输出
    # 需要了解这个方法转换出的数据类型
    # 推断：输出字符串
    # 从read方法中读取数据
    def data_receive(self):
        # print(self.hexShow(self.connect.ser.read_all()))
        print('接受数据中')
        # try:
        #     num = self.ser.inWaiting()
        # except:
        #     # 关闭端口
        #     self.port_close()
        #     return None
        #
        # # 如果接受到数据
        # if num > 0:
        #     data = self.ser.read(num)
        #     num = len(data)
        #     # hex显示
        #     if self.hex_receive.checkState():
        #         out_s = ''
        #         for i in range(0, len(data)):
        #             out_s = out_s + '{:02X}'.format(data[i]) + ' '
        #         self.s2__receive_text.insertPlainText(out_s)
        #     else:
        #         # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
        #         self.s2__receive_text.insertPlainText(data.decode('utf-8'))
        #
        #     # 统计接收字符的数量
        #     self.data_num_received += num
        #     self.lineEdit.setText(str(self.data_num_received))
        #
        #     # 全选
        #     # 获取到text光标
        #     textCursor = self.s2__receive_text.textCursor()
        #     # 滚动到底部
        #     textCursor.movePosition(textCursor.End)
        #     # 设置光标到text中去
        #     self.s2__receive_text.setTextCursor(textCursor)
        # else:
        #     pass

    #该方法为一个槽，与clicked连接
    def buttonClicked(self):

        #设置在输出文本框输出文字
        #输出的内容为data_sender方法中接受的数据
        self.JieShouText.append(self.ShuRuText.toPlainText())





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Version01 = QtWidgets.QWidget()
    ui = Ui_Version01()
    ui.setupUi(Version01)
    Version01.show()
    sys.exit(app.exec_())
