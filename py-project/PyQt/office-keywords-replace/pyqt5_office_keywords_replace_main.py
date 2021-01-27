#导入程序运行必须模块
from win32com.client import Dispatch
import sys
import os
import time
import shutil

#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow,QGroupBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QTextEdit, QInputDialog, QFileDialog, QMessageBox, QDesktopWidget

#导入UI文件类
from pyqt5_office_keywords_replace_ui import Ui_MainWindow

class MyMainForm(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        # 添加选择替换目录 按钮信号和槽
        self.ori_dir_btn.clicked.connect(self.replacePath)

        # 添加添加选择存储目录 按钮信号和槽
        self.replace_dir_btn.clicked.connect(self.savePath)

        #添加开始转换按钮信号和槽
        self.start_transfer.clicked.connect(self.transfer)
        self.word = Dispatch('kwps.Application')

    #需要替换的目录
    def replacePath(self):
        path = QFileDialog.getExistingDirectory(self, "请选择您要替换的目录")
        # 判断选择的文件是否存在
        if os.path.exists(path):
            # 将保存url放入路径文本框中
            self.ori_dir_input.setText(path)
        else:
            self.showMsg('错误', '您选择的目录不存在，请重新选择！')

    def savePath(self):
        path = QFileDialog.getExistingDirectory(self, "请选择您要保存的位置")
        if os.path.exists(path):
            # 将保存url放入路径文本框中
            self.replace_dir_input.setText(path)
        else:
            self.showMsg('错误', '您选择的目录不存在，请重新选择！')


    # 显示消息
    def showMsg(self, tit, content, icon=3):
        box = QMessageBox(QMessageBox.Question, tit, content)
        # 设置左上角消息框图标
        # box.setWindowIcon(QIcon(r'E:\site\python\cutimg\favicon.ico'))
        # 添加按钮，可用中文
        yes = box.addButton('确定', QMessageBox.YesRole)
        # 设置消息框中内容前面的图标
        box.setIcon(icon)
        # 显示该问答框
        box.exec()

    #开始转换
    def transfer(self):

        #需要替换的目录
        self.replace_dir = self.ori_dir_input.text()
        #保存的目录
        self.save_dir = self.replace_dir_input.text()
        #关键词
        self.keywords = self.replace_words.toPlainText()

        if not os.path.isdir(self.replace_dir) or not os.path.isdir(self.save_dir):
            self.showMsg('错误', '您选择的目录不存在，请重新选择！')

        if self.keywords == "":
            self.showMsg('错误', '关键词不能为空')

        #存储目录不存在就直接创建
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)


        #开始替换
        self.replace_tool()
        #将转换结果输出到界面上
        # self.result_display.setPlainText(self.keywords)


    #删除目录及目录下的所有文件
    def del_dir(self, del_path):
        del_list = os.listdir(del_path)
        for f in del_list:
            file_path = os.path.join(del_path, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    #将doc替换成docx
    def doc2docx(self, file):
        file = file.replace('\\', '/')
        file_dir, tmpfilename = os.path.split(file)
        file_name, extension = os.path.splitext(tmpfilename)
        # self.result_display.setPlainText(file_name+"\n"+file_dir+"\n"+extension)
        doc = self.word.Documents.Open(file)
        doc.SaveAs(file_dir + "/" +file_name + '.docx', 12)  #12表示docx格式
        doc.Close()
        #删除doc文件
        os.remove(file)

    #将目录及子目录下的文件copy到另一个目录
    def deep_copy_dir(self, origin_dir, target_dir):
        for files in os.listdir(origin_dir):
            name = os.path.join(origin_dir, files)
            back_name = os.path.join(target_dir, files)
            if os.path.isfile(name):
                if os.path.isfile(back_name):
                    shutil.copy(name, back_name)
                else:
                    shutil.copy(name, back_name)
            else:
                if not os.path.isdir(back_name):
                    os.makedirs(back_name)
                self.deep_copy_dir(name, back_name)

    #获取目录及子目录下的文件，并转换成可以处理的格式
    def recurse_transfer_file(self, path):
        for root, dirs, files in os.walk(path):
            for file in files:
                # self.result_display.setPlainText(file+"\n"+docx_name)
                # 判断同名的docx文件是否存在如果存在，则删除doc文件不进行转换
                src_file = os.path.join(root, file)
                if src_file.endswith(".doc") and not src_file.startswith('~$'):
                    # self.result_display.setPlainText(src_file)
                    self.doc2docx(src_file)
        self.word.Quit()


    #文件关键字替换
    # def file_keywords_replace(self, file):
    #     doc = self.word.Documents.Open(file)
    #         line = f.readline()
    #         if line:
    #             split_list = line.split('|')
    #             old_word = split_list[0].replace('\r', '').replace('\n', '').replace('\t', '')
    #             new_word = split_list[1].replace('\r', '').replace('\n', '').replace('\t', '')
    #             self.word.Selection.Find.Execute(old_word, False, False, False, False, False, True, 1, True, new_word, 2)
    #             file_name = file_name.replace(old_word, new_word)
    #         else:
    #             break
    #     # doc.SaveAs(file)
    #     # print("{0}{1}.docx".format(result_dir, file_name))
    #
    #     doc.SaveAs(r"{0}{1}.docx".format(result_dir, file_name))
    #     if origin_file_name != file_name:
    #         os.remove(file)
    #     doc.Close()


    #核心替换功能
    def replace_tool(self):
        # 转换前先清空目录下文件
        self.del_dir(self.save_dir)
        #将原始目录及子目录文件全部拷贝至新目录
        self.deep_copy_dir(self.replace_dir, self.save_dir)
        #递归处理存储目录下的文件
        self.recurse_transfer_file(self.save_dir)
        # self.result_display.setPlainText(self.save_dir)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())