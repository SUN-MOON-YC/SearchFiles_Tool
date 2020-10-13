#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：yangchao  albert time:2020/9/4
"""
   说明：
"""

from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
import seach_main,HZcode,KeyStrCode,AllUICode
import sys
from PyQt5 import QtCore
class StartWin(QMainWindow,seach_main.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        seach_main.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # 添加触发
        self.action_key.triggered.connect (self.open_show_key)
        self.action.triggered.connect (self.open_show_hz)
        self.action_3.triggered.connect (self.open_show_allui)
        self.action_4.triggered.connect (self.about)
    # 定义打开窗口函数
    def open_show_key(self):
        self.win = KeyStrCode.KeyCode ()
        self.win.setupUi (self.win)
        # 添加查找的原始路径触发
        self.win.pushButton_selectSourcePath.clicked.connect (self.win.getPath)
        # self.win.checkBox_C.stateChanged.connect (self.win.setSourcePath)
        # self.win.checkBox_D.stateChanged.connect (self.win.setSourcePath)
        # self.win.checkBox_E.stateChanged.connect (self.win.setSourcePath)
        # self.win.lineEdit.textChanged.connect(self.win.setKeys)
        # self.win.lineEdit_2.textChanged.connect (self.win.setKeys)
        # self.win.lineEdit_3.textChanged.connect (self.win.setKeys)
        # self.win.lineEdit.editingFinished.connect (self.win.setKeys)
        # self.win.lineEdit_2.editingFinished.connect (self.win.setKeys)
        # self.win.lineEdit_3.editingFinished.connect (self.win.setKeys)
        # 添加查找按钮触发
        self.win.pushButton_search.clicked.connect (self.win.preparedForSearch)
        # 添加复制文件路径和开始复制的触发
        self.win.pushButton_selectTargetPath.clicked.connect (self.win.setCopyPath)
        self.win.pushButton_copy.clicked.connect (self.win.copyFiles)
        # 展示窗体
        self.win.show ()

    def open_show_hz(self):
        self.HZwin = HZcode.HZcode ()
        self.HZwin.setupUi (self.HZwin)

        #添加查找的原始路径触发
        self.HZwin.pushButton_selectSourcePath.clicked.connect (self.HZwin.getPath)
        # self.HZwin.checkBox_C.stateChanged.connect (self.HZwin.selectSourcePath)
        # self.HZwin.checkBox_D.stateChanged.connect (self.HZwin.selectSourcePath)
        # self.HZwin.checkBox_E.stateChanged.connect (self.HZwin.selectSourcePath)
        # # 添加选择文件后缀的触发
        # self.HZwin.checkBox_pdf.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_txt.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_doc.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_docx.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_csv.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_xlsx.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_xls.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_html.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_py.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_rar.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_png.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_jpg.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_bmp.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_gif.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_ico.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_flv.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_wmv.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_avi.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_rm.stateChanged.connect (self.HZwin.filename_extension_lists)
        # self.HZwin.checkBox_mp4.stateChanged.connect (self.HZwin.filename_extension_lists)
        # 添加查找按钮触发
        self.HZwin.pushButton_search.clicked.connect (self.HZwin.search_File)
        #添加复制文件路径和开始复制的触发
        self.HZwin.pushButton_selectTargetPath.clicked.connect (self.HZwin.setCopyPath)
        self.HZwin.pushButton_copy.clicked.connect(self.HZwin.copyFiles)
        #展示窗体
        self.HZwin.show()

    def open_show_allui(self):
        self.all=AllUICode.AllUICode()
        self.all.setupUi(self.all)
        #
        self.all.pushButton_selectSourcePath.clicked.connect (self.all.getPath)
        # 添加查找按钮触发
        self.all.pushButton_search.clicked.connect (self.all.preparedForSearch)
        # 添加复制文件路径和开始复制的触发
        self.all.pushButton_selectTargetPath.clicked.connect (self.all.setCopyPath)
        self.all.pushButton_copy.clicked.connect (self.all.copyFiles)
        # 展示窗体
        self.all.show ()

    def about(self):
        QMessageBox.information (None, '关于', '''（1）	开发的背景说明
笔者性格比较随意的缘故，工作过程中经常有些重要的文件存放路径被忘记。特别是有时急着使用，凭记忆在电脑中到处翻看，费时费力，经常查找没有结果，急得让人想跳脚砸电脑。利用电脑系统的查找功能，条件输入比较麻烦，而且效率也不高，关键查到文件还不能自动处理文件（复制到指定路径）。
比如：查找电脑中所有的包含关键字“周报”的excel文件，并自动复制放在桌面文件夹” C:\\Users\\Administrator\\Desktop\\results”中。
比如：客户提供多个Excel文件，有关联字段，需要进行数据的维护。如挑选出不同的数据（异常数据）、数据合并、数据筛选等
由于多次遇到领导安排类似的工作任务，手动处理几次后发现耗费时间不说还经常出错，被折磨修改好几回。
痛定思痛决定利用所学的知识，编写个小工具来完成任务，解放自己的大脑。（2）	介绍
主要介绍三种查询文件方式，一是通过文件后缀查询，二是通过文件名称中关键字查询，三是结合前面的综合查询。
注意，待查询文件的可能路径可设定，也可选定多个磁盘根路径（D盘，E盘）；输入关键字，选定文件后缀（可多选，可自定义后缀），点击“开始查询”后耐心等待查询结果；查询完毕，选定复制的目标文件夹，点击“开始复制”即可。
''', QMessageBox.Ok)



if __name__=='__main__':
    app = QApplication (sys.argv)
    ui = StartWin()
    ui.show ()
    sys.exit (app.exec_ ())
