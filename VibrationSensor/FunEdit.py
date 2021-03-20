# -*- coding: utf-8 -*-
# @Time    : 2021/1/23 16:12
# @Author  : Zeeland
# @File    : FunEdit.py
# @Software: PyCharm

#导包
from Main import Ui_Form
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox,QLineEdit
import pyqtgraph as pg
from PyQt5.QtCore import QTimer,QRect,QThread,pyqtSignal
import serial
import serial.tools.list_ports
import sys
import pymysql

#创建检测串口线程
# class serialThread(QThread):
#     oneSecondTriger = pyqtSignal()
#
#     def __init__(self):
#         super(serialThread,self).__init__()
#
#     def run(self):
#         while True:
#             self.oneSecondTriger.emit()
#             time.sleep(1)



#创建Edit类,继承在Qtdesigne做好的Ui_Form，继承QWidget控件的特性
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
        self.pushButton_3_RealTimeData.setEnabled(False)

        #设置passwordEdit的可见性
        self.lineEdit_1_localPwd.setEchoMode(QLineEdit.Password)
        self.lineEdit_1_cloudPwd.setEchoMode(QLineEdit.Password)

        #添加图表控件
        self.graphicsView = pg.PlotWidget(self.tab_3)
        self.graphicsView.setGeometry(QRect(20, 20, 951, 351))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.plot(
            [1, 2, 3, 4, 5, 6, 10, 11, 22, 11, 222, 11, 1, 1, 1, 1, 1, 2, 5, 10, 6, 3, 6, 4, 64, 54, 5, 45, 4, 1],
            pen='r', symbol='o')


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


    #创建按键绑定信号
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

        #定时发送数据：点击后发送同时接受数据
        self.pushButton_3_RealTimeData.clicked.connect(self.data_send_setting)
        #一个QTimer实例
        self.timer_send = QTimer(self)
        #用QTimer执行周期性发送数据的功能
        self.timer_send.timeout.connect(self.data_send)

        #关闭定时发送数据
        self.pushButton_3_Stop.clicked.connect(self.data_send_close)

        # 定时器接收数据
        self.timer_receive = QTimer(self)
        self.timer_receive.timeout.connect(self.data_receive)

        # 清除窗口数据
        self.pushButton_5_clear.clicked.connect(self.send_data_clear)


        #检测串口线程
        # self.timeThread = serialThread()
        # self.timeThread.oneSecondTriger.connect(self.port_check)
        # #在串口连接成功后关闭线程
        # self.timeThread.start()

        #数据校准
        self.pushButton_2_DataCalibration.clicked.connect(self.data_reset)

        #数据初始化
        self.pushButton_2_init.clicked.connect(self.data_init)

        #修改参数
        self.pushButton_2_QueDing.clicked.connect(self.data_modify)

        #保存配置
        self.pushButton_2_save.clicked.connect(self.data_AttributeSave)

        #导入配置
        self.pushButton_2_InputData.clicked.connect(self.data_inputData)

        #导出配置
        self.pushButton_2_OutputData.clicked.connect(self.data_outputData)

        #保存数据到本地
        self.pushButton_5_SaveToFile.clicked.connect(self.data_saveLocally)

        #本地数据库连接
        self.pushButton_1_localMysqlConnect.clicked.connect(self.localMysql_connect)

        #云端数据库连接
        self.pushButton_1_cloudMysqlConnect.clicked.connect(self.cloudMysql_connect)


    """
    这里为函数工作台
    ---------------------------------------------------------------
    ---------------------------------------------------------------
    """
    def cloudMysql_connect(self):
        self.cloudhost = self.lineEdit_1_cloudHost.text()
        self.clouduser = self.lineEdit_1_cloudAccount.text()
        self.cloudPwd = self.lineEdit_1_cloudPwd.text()
        self.cloudDBName = self.lineEdit_1_cloudDBName.text()
        self.cloudPort = int(self.lineEdit_1_cloudPort.text())

        try:
            #这里需要多线程！！！！
            # 连接数据库
            self.cloudConn = pymysql.connect(host=self.cloudhost, user=self.clouduser,
                                             password=self.cloudPwd, db=self.cloudDBName,port=self.cloudPort)

            # self.cloudConn = pymysql.connect(host='rm-bp1o0649d1hoda9z2wo.mysql.rds.aliyuncs.com', user='user01',
            #                        password='Lzn123456',
            #                        db='vibrationsensor', port=3306, charset='utf8')
            QMessageBox.about(self,'message','连接成功')
            self.cursor = self.cloudConn.cursor()
        except Exception as e:
            QMessageBox.critical(self,'warning','连接失败')
            print(e)

    #本地mysql数据库连接
    def localMysql_connect(self):
        self.localhost = self.lineEdit_1_localHost.text()
        self.localuser = self.lineEdit_1_localAccount.text()
        self.localPwd = self.lineEdit_1_localPwd.text()
        self.localDBName = self.lineEdit_1_localDBName.text()
        try:
            # 打开数据库
            # 这里需要多线程！！！！
            '''-----------------------存在问题尚未处理：变量带入后无法连接成功，正在寻找原因-----------------------------------'''
            self.localConn = pymysql.connect(host=self.localhost, user=self.localuser,
                                      password=self.localPwd, database=self.localDBName)
            QMessageBox.about(self,"message","连接成功")
        except:
            QMessageBox.critical(self,"warning","连接失败，出现异常")

    #数据本地保存
    def data_saveLocally(self):
        pass


    #导出配置
    #将所有的数据按照顺序保存
    def data_outputData(self):
        QMessageBox.about(self, "message", "暂未实现")

    #导入配置
    #导入配置需要一套自己的文件读写规范
    def data_inputData(self):
        QMessageBox.about(self,"message","暂未实现")

    #保存配置，保存配置意味着下次打开的界面配置还是现在的情况
    def data_AttributeSave(self):
        QMessageBox.about(self,"message","暂未实现")

    def data_modify(self):
        QMessageBox.about(self,"message","暂未实现")


    '''----------------------------待测试--------------------------------------------'''
    # 数据复位设置
    def data_reset(self):
        try:
            # 写入重置数据的参数
            # 恢复出厂配置
            self.ser.write(bytes([0x01, 0x06, 0x00, 0x7F, 0x00, 0x01, 0x79, 0xD2]))
            # 确认发送
            self.ser.write(bytes([0x01, 0x06, 0x00, 0xC7, 0x00, 0x01, 0xF9, 0xF7]))

            QMessageBox.about(self, "message", "复位成功")
        except:
            QMessageBox.critical(self, 'Error', '重置错误')


    '''----------------------------待测试--------------------------------------------'''
    #恢复出厂设置(初始化)
    def data_init(self):
        try:
            #写入重置数据的参数
            # 恢复出厂配置
            self.ser.write(bytes([0x01, 0x06, 0x00, 0x7F, 0x00, 0x01, 0x79, 0xD2]))
            # 确认发送
            self.ser.write(bytes([0x01, 0x06, 0x00, 0xC7, 0x00, 0x01, 0xF9, 0xF7]))

            QMessageBox.about(self,"message","恢复出厂设置成功")
        except:
            QMessageBox.critical(self,'Error','重置错误')

    #画图的方法
    def draw(self):
        pass


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

        # 打开串口接收定时器，周期为100ms
        self.timer_receive.start(20)

        if self.ser.isOpen():
            self.pushButton_1_LianJie.setEnabled(False)
            self.pushButton_1_DuanKaiLianJie.setEnabled(True)
            self.pushButton_3_RealTimeData.setEnabled(True)
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
        #传入毫秒数
        self.timer_send.start(int(self.textEdit_3_OutputFrequency.toPlainText()))
        #开始定时接受数据
        QMessageBox.about(self,"Message","正在实时发送数据")
        self.pushButton_3_RealTimeData.setEnabled(False)
        self.pushButton_3_Stop.setEnabled(True)




    #QTimer需要周期性执行向串口发送信息的内容
    def data_send(self):
        self.ser.write(bytes([0x01, 0x04, 0x01, 0xA1, 0x00, 0x17, 0xE0, 0x1A]))# 向传感器发送一个一个16进制数组
        self.data_num_sended = self.data_num_sended + 8 #已接收的数据量+8
        self.textBrowser_5_send.setText(str(self.data_num_sended))

        # self.receive_data = self.ser.read_all()
        # print(self.receive_data)


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



    # '''
    # 将bytes的16进制表示转换为字符串10进制表示形式
    # '''
    # def hexShow(self):
    #
    #     try:
    #         result = ''
    #         hLen = len(self.receive_data)
    #         for i in range(hLen):
    #             mid = self.receive_data[i]
    #
    #             # 不足两位，则补0,以16进制表示bytes数据流
    #             # hhex为单个元素
    #
    #             hhex = '%02x' % mid
    #             result += hhex + ' '
    #         return result
    #     except Exception as e:
    #         print("---异常---：", e)
    #
    #
    # '''
    # 将bytes类型的data转换为数组
    # '''
    # def hexArray(self):
    #     arr = []
    #     try:
    #         result = ''
    #         hLen = len(self.receive_data)
    #         for i in range(hLen):
    #             mid = self.receive_data[i]
    #
    #             # 不足两位，则补0,以16进制表示bytes数据流
    #             # hhex为单个元素
    #             hhex = '%02x' % mid
    #             arr.append(hhex)
    #         return arr
    #     except Exception as e:
    #         print("---异常---：", e)
    #
    # def data_receive(self):
    #     if self.pushButton_3_RealTimeData.isDown() & self.checkBox_5_DisplayInput.isChecked():
    #         try:
    #             #接受到的传感器信息
    #             self.receive_data =self.ser.read_all()
    #             #将信息转换为数组形式
    #             self.arr =self.hexArray()
    #             print(self.receive_data)
    #             #数组数据解析
    #             self.analyse()
    #             #在数据流中显示信息
    #             self.receive_str = '接受:'+ str(self.hexShow())
    #             self.textBrowser_5_receive.setText(self.receive_str)
    #         except Exception as e:
    #             print('Warning:',e)




    #在底层数据流中的文本框中显示
    #要先判断是否选中在底层数据流接受数据
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
                self.arr = out_s.split()#arr是一个数组
                print(self.arr)


                #如果产生一场数据，则抛弃
                #双重判断,04为功能码
                if len(self.arr)==51 and self.arr[1]=="04":
                    # arr为接受到数据的数组
                    # 调用数据分析函数
                    # 即点击了实时数据的pushButton才能启动数据分析模式
                    # 方法串口接口到无效信息导致乱码
                    self.analyse()

                    self.textBrowser_5.append("接收:" + out_s)
                    self.data_num_received += num
                    #设置接受数据
                    self.textBrowser_5_receive.setText(str(self.data_num_received))
                else:
                    pass




    '''
    数据样本：
    正常状态下len(self.arr)=51
    
    ['01', '04', '2E', '00', '49', '00', '2F', '00', '2A', '00', '00', '00', '32', '00', '5A', '00', '00', '00', '0A', '00', '96', '00', '00', '00', '00', '00', '50', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '01', '0E', '00', '00', 'FC', 'C6']
    [0       1    2      3    4     5      6    7      8   9      10     11   12     13   14     15    16   17   18     19    20   21    22     23    24    25   26     27   28    29     30    31    32   33    34    35     36    37  38       39   40    41     42   43    44   45    46     47    48     49   50]
    [ 地址码     数据长度 频率：X          Y          z                                                                                                                                                                                                                              温度    温度报警      CRC    ]
    '''
    # 数据分析
    def analyse(self):
        #self.temperture =

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

        # 振幅可视化
        self.textBrowser_3_X_Amplitude.setText(str((int(self.arr[13] + self.arr[14], 16) / 10)))
        self.textBrowser_3_Y_Amplitude.setText(str((int(self.arr[19] + self.arr[20], 16) / 10)))
        self.textBrowser_3_Z_Amplitude.setText(str((int(self.arr[25] + self.arr[26], 16) / 10)))



    # 清除显示
    def send_data_clear(self):
        self.textBrowser_5.setText("")
        self.textBrowser_5_receive.setText("0")
        self.textBrowser_5_send.setText("0")


if __name__ == '__main__':
    #import qdarkstyle
    app = QApplication(sys.argv)
    myshow =  Edit()
    myshow.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    sys.exit(app.exec_())
