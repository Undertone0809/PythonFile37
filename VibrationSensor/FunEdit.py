# -*- coding: utf-8 -*-
# @Time    : 2021/1/23 16:12
# @Author  : Zeeland
# @File    : FunEdit.py
# @Software: PyCharm

#导包
from Main import Ui_Form
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox
from PyQt5.QtCore import QTimer,QDateTime
import serial
import serial.tools.list_ports
import sys

#创建Edit类
class Edit(Ui_Form,QWidget):
    #定义初始化进程
    def __init__(self):
        #继承
        super().__init__()
        #往空QWidget中放置UI内容
        self.setupUi(self)
        self.setWindowTitle("VibrationSenorTool 1.0")

        #设置一些PushButton的可见性
        self.pushButton_3_Stop.setEnabled(False)

        # 创建一系列信号
        self.init()
        #创建一个空串口对象
        self.ser =serial.Serial()
        #检测串口
        self.port_check()

        #计数初始化
        self.data_num_received =0
        self.textBrowser_5_receive.setText(str(self.data_num_received))
        self.data_num_sended =0
        self.textBrowser_5_send.setText(str(self.data_num_sended))

        """
        这里检测串口要开多线程！！！！！
        """


    #创建信号
    def init(self):
        #串口检测
        self.pushButton_1_JianCeChuanKou.clicked.connect(self.port_check)

        #串口信息显示
        #当下拉索引发生改变时发射信号触发绑定的事件
        self.comboBox_1_1.currentTextChanged.connect(self.port_info)

        # 打开串口按钮
        self.pushButton_1_LianJie.clicked.connect(self.port_open)

        #关闭串口
        self.pushButton_1_DuanKaiLianJie.clicked.connect(self.port_close)

        #定时发送数据
        self.pushButton_3_RealTimeData.clicked.connect(self.data_send_setting)
        #一个QTimer实例
        self.timer_send = QTimer()
        #用QTimer执行周期性发送数据的功能
        self.timer_send.timeout.connect(self.data_send)

        #关闭定时发送数据
        self.pushButton_3_Stop.clicked.connect(self.data_send_close)

        # 定时器接收数据
        self.timer_receive = QTimer(self)
        self.timer_receive.timeout.connect(self.data_receive)

        # 清除发送窗口
        self.pushButton_5_clear.clicked.connect(self.send_data_clear)


    """
    这里为函数工作台
    ---------------------------------------------------------------
    ---------------------------------------------------------------
    """

    # 在底层数据流中的文本框中显示
    # 要先判断是否选中在底层数据流接受数据
    def data_receive(self):
        if self.checkBox_5_DisplayInput.isChecked():
            try:
                #num返回接收缓存中的字节数
                num = self.ser.inWaiting()
            except:
                self.port_close()
                return None
            if num > 0:
                #读取所有字节
                data = self.ser.read(num)
                #num返回所有字节的长度
                num = len(data)
                # hex显示
                out_s = ''
                for i in range(0, len(data)):
                    out_s = out_s + '{:02X}'.format(data[i]) + ' '
                self.textBrowser_5.append("接收:" + out_s)
                self.arr = out_s.split()
                # arr为接受到数据的数组
                # 调用数据分析函数
                # 即点击了实时数据的pushButton才能启动数据分析模式
                # 方法串口接口到无效信息导致乱码
                self.analyse()

                self.data_num_received += num
                self.textBrowser_5_receive.setText(str(self.data_num_received))





    """
    -----------------------------------------------------------------------
    -----------------------------------------------------------------------
    """


    #检测串口的方法
    def port_check(self):
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox_1_1.clear()
        # 添加到menu中
        for port in port_list:
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]
            self.comboBox_1_1.addItem(port[0])
        #如果数组中没有内容
        if len(self.Com_Dict) == 0:
            self.label_1_PortInfo.setText("无串口")

    # 串口信息
    def port_info(self):
        # 显示选定的串口的详细信息
        #显示下拉菜单栏中现在文本
        imf_s = self.comboBox_1_1.currentText()
        if imf_s != "":
            #显示串口信息
            self.label_1_PortInfo.setText(self.Com_Dict[self.comboBox_1_1.currentText()])

    #打开串口
    def port_open(self):
        # 传入参数
        self.ser.port = self.comboBox_1_1.currentText()
        self.ser.baudrate = 115200
        self.ser.bytesize = 8
        self.ser.stopbits = 1
        self.ser.parity = "N"
        self.ser.timeout = 0.01
        #弹窗：测试连接成功
        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None

        # 打开串口接收定时器，周期为2ms
        self.timer_receive.start(2)

        if self.ser.isOpen():
            self.pushButton_1_LianJie.setEnabled(False)
            self.pushButton_1_DuanKaiLianJie.setEnabled(True)
            QMessageBox.about(self,"Port Information","连接成功")


    # 关闭串口
    def port_close(self):
        #定时接受数据的timer
        self.timer_receive.stop()
        #定时发送数据的timer
        self.timer_send.stop()
        #抛出异常
        try:
            self.ser.close()
        except :
            pass
        if self.ser.isOpen() is not True:
            #弹出关闭信息
            QMessageBox.about(self,"Port Information","串口已关闭")
            self.pushButton_1_DuanKaiLianJie.setEnabled(False)
            self.pushButton_1_LianJie.setEnabled(True)

        # # 接收数据和发送数据数目置零
        # self.data_num_received = 0
        # self.lineEdit.setText(str(self.data_num_received))
        # self.data_num_sended = 0
        # self.lineEdit_2.setText(str(self.data_num_sended))
        # self.Form01GroupBox1.setTitle("串口状态（已关闭）")


    #设定运行周期
    def data_send_setting(self):
        self.timer_send.start(int(self.textEdit_3_OutputFrequency.toPlainText()))
        QMessageBox.about(self,"Message","正在实时发送数据")
        self.pushButton_3_RealTimeData.setEnabled(False)
        self.pushButton_3_Stop.setEnabled(True)




    #QTimer需要周期性执行的内容
    def data_send(self):
        # 传入一个16进制数组
        self.ser.write(bytes([0x01, 0x04, 0x01, 0xA1, 0x00, 0x17, 0xE0, 0x1A]))
        self.data_num_sended = self.data_num_sended + 8
        self.textBrowser_5_send.setText(str(self.data_num_sended))

        if self.checkBox_5_DisplayOutput.isChecked():
            #在底层数据流中显示发送和接收的信息
            self.textBrowser_5.append("发送:01 04 01 A4 00 17 E0 1A")
        else:
            pass


    #关闭定时发送功能
    def data_send_close(self):
        self.timer_send.stop()
        QMessageBox.about(self,"Message","已关闭")
        self.pushButton_3_Stop.setEnabled(False)
        self.pushButton_3_RealTimeData.setEnabled(True)




    # 数据分析
    def analyse(self):
        # 温度可视化
        # 转换后的温度除10
        self.textBrowser_3_Temperture.setText(str((int(self.arr[45] + self.arr[46], 16) / 10)))

        # 频率可视化
        self.textBrowser_3_Frequency_X.setText(str((int(self.arr[3] + self.arr[4], 16))))
        self.textBrowser_3_Frequency_Y.setText(str((int(self.arr[5] + self.arr[6], 16))))
        self.textBrowser_3_Frequency_Z.setText(str((int(self.arr[7] + self.arr[8], 16))))

        # 加速度可视化
        self.textBrowser_3_X_Acceleration.setText(str((int(self.arr[9] + self.arr[10], 16) / 10)))
        self.textBrowser_3_Y_Acceleration.setText(str((int(self.arr[15] + self.arr[16], 16) / 10)))
        self.textBrowser_3_Z_Acceleration.setText(str((int(self.arr[21] + self.arr[22], 16) / 10)))

        # 速度可视化
        self.textBrowser_3_X_Speed.setText(str((int(self.arr[11] + self.arr[12], 16) / 10)))
        self.textBrowser_3_Y_Speed.setText(str((int(self.arr[17] + self.arr[18], 16) / 10)))
        self.textBrowser_3_Z_Speed.setText(str((int(self.arr[23] + self.arr[24], 16) / 10)))

        # 位移可视化
        self.textBrowser_3_X_Amplitude.setText(str((int(self.arr[13] + self.arr[14], 16) / 10)))
        self.textBrowser_3_Y_Amplitude.setText(str((int(self.arr[19] + self.arr[20], 16) / 10)))
        self.textBrowser_3_Z_Amplitude.setText(str((int(self.arr[25] + self.arr[26], 16) / 10)))





    # 清除显示
    def send_data_clear(self):
        self.textBrowser_5.setText("")


if __name__ == '__main__':
    import qdarkstyle
    app = QApplication(sys.argv)
    myshow =  Edit()
    myshow.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    sys.exit(app.exec_())
