import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QMessageBox,QPushButton,QVBoxLayout
from PyQt5 import QtCore
import pyqtgraph as pg
import numpy as np


class TestWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        # 设置窗体尺寸
        self.setGeometry(300, 300, 500, 350)
        # 添加一个按钮和一个PlotWidget
        self.draw_fig_btn = QPushButton("绘图")
        self.draw_fig_btn.setFixedWidth(100)#设置Button宽度
        self.plt = pg.PlotWidget(background="w")
        # 将两个Widget垂直排列布局
        # MainWindow的主体内容要通过一个widget包裹在一起，通过self.setCentralWidget设置
        centralWidget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.draw_fig_btn)
        main_layout.addWidget(self.plt)
        centralWidget.setLayout(main_layout)
        # 应用上述布局
        self.setCentralWidget(centralWidget)
        # 为[绘图]按钮注册一个回调函数
        self.draw_fig_btn.clicked.connect(self.draw_fig_btn_cb)


class mywindow(QWidget, TestWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        x = np.linspace(-100, 100, 1000)
        data = np.tan(x) / x
        self.graphicsView = pg.PlotWidget(self)
        self.graphicsView.setGeometry(QtCore.QRect(100, 100, 500,500))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.sizePolicy=["Fixed","Fixed",0,10]
        self.pushButton.clicked.connect(self.handclick)
        self.graphicsView.plot(data, pen='g')
        self.label = pg.TextItem(text="横坐标：{}".format(0))
        self.label1 = pg.TextItem(text="纵坐标：{}".format(0), anchor=(0, -1))
        self.graphicsView.addItem(self.label)
        self.graphicsView.addItem(self.label1)
        self.setMouseTracking(True)
        self.graphicsView.scene().sigMouseMoved.connect(self.onMouseMoved)
    def onMouseMoved(self, evt):
        if self.graphicsView.plotItem.vb.mapSceneToView(evt):
            point =self.graphicsView.plotItem.vb.mapSceneToView(evt)
            self.label.setHtml("<p style='color:white'>横坐标：{0}</p>".format(point.x()))
            self.label1.setHtml("<p style='color:white'>纵坐标: {0}</p>".format(point.y()))
    def handclick(self):
        QMessageBox.about(self,'1','1')

if __name__ =="__main__":
    app = QApplication(sys.argv)
    w = mywindow()
    w.show()
    sys.exit(app.exec_())
