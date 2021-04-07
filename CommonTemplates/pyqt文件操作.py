from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt5.QtCore import QFile,QUrl
import sys,os
from Form import Ui_Form



class FileOperation(QWidget, Ui_Form):
    def __init__(self):
        super(FileOperation, self).__init__()
        self.setupUi(self)
        self.init()

    #信号与槽绑定
    def init(self):
        self.pushButton_readFile.clicked.connect(self.readFile)
        self.pushButton_writeFile.clicked.connect(self.writeFile)
        self.pushButton_1.clicked.connect(self.slot_btn_chooseFile)

    def readFile(self):
        fname = QFileDialog.getOpenFileName(self, "Open File","./", "All Files(*);;Wav(*.wav);;Txt (*.txt)")
        # 该方法返回一个tuple,里面有两个内容，第一个是路径， 第二个是要打开文件的类型，所以用两个变量去接受
        # 如果用户主动关闭文件对话框，则返回值为空
        if fname[0]:  # 判断路径非空
            f = QFile(fname[0])  # 创建文件对象，不创建文件对象也不报错 也可以读文件和写文件
            # open()会自动返回一个文件对象
            f = open(fname[0], "r")  # 打开路径所对应的文件， "r"以只读的方式 也是默认的方式
            with f:
                data = f.read()
                print(data)
                #self.textEdit.setText(data)
            f.close()


    #选择文件
    def slot_btn_chooseFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,"选取文件",self.cwd,
                                                                "All Files (*);;Text Files (*.txt)")
        # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            print("\n取消选择")
            return

        print("\n你选择的文件为:")
        print(fileName_choose)
        print("文件筛选器类型: ", filetype)

    def writeFile(self):
        fname = QFileDialog.getSaveFileName(self, "Write File", self.cwd, "Wav(*.wav);;All (*.*)")  # 写入文件首先获取文件路径
        if fname[0]:  # 如果获取的路径非空
            f = open(fname[0], "w")  # 以写入的方式打开文件
            with f:
                data = self.textEdit.toPlainText()  # 获取textEdit的str
                f.write(data)
        f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FileOperation()
    win.show()
    sys.exit(app.exec())