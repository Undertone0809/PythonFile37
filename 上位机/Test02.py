from PyQt5.Qt import *
import pyqtgraph as pg
from PyQt5 import QtCore

# pg.setConfigOption('background', 'w')#设置=背景
# pg.setConfigOption('foreground', 'k')

# 继承控件 QWidget
class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Window 实例尺寸
        self.resize(600,600)
        # 创建一个控件PlotWidget
        self.plotWidget_ted = pg.PlotWidget(self)
        # 设置 PlotWidget 位置尺寸
        self.plotWidget_ted.setGeometry(QtCore.QRect(25, 25, 550, 550))
        # 作图
        #传入一个数组，进行绘图
        self.plotWidget_ted.plot([1,2,3,4,5,6,10,11,22,11,222,11,1,1,1,1,1,2,5,10,6,3,6,4,64,54,5,45,4,1],pen='r',symbol='o')

    def onMouseMoved(self, evt):
        if self.graphicsView.plotItem.vb.mapSceneToView(evt):
            point = self.graphicsView.plotItem.vb.mapSceneToView(evt)
            self.label.setHtml("<p style='color:white'>横坐标：{0}</p>".format(point.x()))
            self.label1.setHtml("<p style='color:white'>纵坐标: {0}</p>".format(point.y()))


if __name__ == '__main__':
    # 该部分以及结束的 sys.exit(app.exec_()) 是固定的 PyQt5 运行语句
    import sys
    app = QApplication(sys.argv)

    # 建立窗口实例并展示
    window = Window()
    window.show()

    sys.exit(app.exec_())

