#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：yangchao  albert time:2020/9/10
"""
   说明：
"""
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QMessageBox
from PyQt5.QtGui import QFont
import all_display
import os
import myfilesearch

class AllUICode(QMainWindow,all_display.Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__ (self)
        all_display.Ui_MainWindow.__init__(self)
        self.setupUi (self)
        # 待查找文件的可能路径
        self.paths = []
        # 待查找文件的关键字
        self.keys = []
        # 待查找文件的后缀
        self.filename_extension = []

        #查找到的目标文件
        self.tarfiles=[]

    def getPath(self):
        try:
            # 选择待查找文件的可能路径
            source_path = QFileDialog.getExistingDirectory (None, "选择待查找文件的可能路径", os.getcwd ())
            self.lineEdit_sourcePath.setText(source_path)
        except Exception:
            QMessageBox.warning (None, '警告', '请选择一个有效路径……', QMessageBox.Ok)
        else:
            print('sourcePath is : {}'.format(source_path))

    def setKeys(self):
        sender = self.sender ()
        if sender ==self.lineEdit and self.lineEdit.text() != '':
            self.keys.append(self.lineEdit.text())
        if sender ==self.lineEdit_2 and self.lineEdit_2.text() != '':
            self.keys.append(self.lineEdit_2.text())
        if sender ==self.lineEdit_3 and self.lineEdit_3.text() != '':
            self.keys.append(self.lineEdit_3.text())
        self.keys=list(set(self.keys))
        print(self.keys)
        return self.keys

    def search_File(self):
        #查找文件
        if len(self.keys)==0:
            for p in self.paths:
                myfilesearch.new_search_file_by_file_type(p,self.filename_extension,self.tarfiles)
        elif len(self.filename_extension)==0:
            for p in self.paths:
                myfilesearch.new_search_file_by_key_str(p,self.keys,self.tarfiles)
        else:
            for p in self.paths:
                myfilesearch.new_search_file_by_all (p, self.keys,self.filename_extension,self.tarfiles)
        self.tarfiles=list(set(self.tarfiles))
        print('findfiles:',self.tarfiles)
        QMessageBox.information (self, '信息', '查询结束！', QMessageBox.Close)
        if len(self.tarfiles) > 0 :
            for num,li in zip(range(1,len(self.tarfiles)+1),self.tarfiles):
                self.textBrowser.append(str(num)+': '+ li +'\n')
                self.textBrowser.setStyleSheet ("color:black")  # 设置颜色
                self.textBrowser.setFont (QFont ("Timers", 9, QFont.Normal))
        else:
            self.textBrowser.append ('按照设定条件没有查找到对应文件！')
            self.textBrowser.setStyleSheet ("color:red")  # 设置颜色
            self.textBrowser.setFont (QFont ("Timers", 12, QFont.Bold))
        #显示查找结果
        self.label_displyFindNum.setText ('total find {} files!'.format (len (self.tarfiles)))
        self.label_displyFindNum.setStyleSheet ("color:red")
        self.label_displyFindNum.setFont (QFont ("Timers", 12, QFont.Bold))

    def preparedForSearch(self):
        # 把选择的自定义路径加到self.paths
        if self.lineEdit_sourcePath.text () != '':
            self.paths.append (self.lineEdit_sourcePath.text ())
        #添加选择的盘路径
        boxs1=[self.checkBox_C,self.checkBox_D,self.checkBox_E]
        for box in boxs1:
           if box.isChecked()==True:
               self.paths.append(box.text())
        self.paths = [os.path.normpath (p) for p in self.paths]  # 转为标准路径
        self.paths = list (set (self.paths))  # 去重
        print ('source_dirs:',self.paths)
        if len (self.paths) == 0:
            QMessageBox.warning (None, '警告', '请先选择一个有效查找路径后再开始查找...', QMessageBox.Ok)
            return

        # 把自定义后缀加到self.filename_extension
        if self.lineEdit_CustomerDefineHZ.text () != '':
            self.filename_extension.append (self.lineEdit_CustomerDefineHZ.text ())
        boxes2 = [self.checkBox_pdf, self.checkBox_txt, self.checkBox_doc,
                 self.checkBox_docx, self.checkBox_csv, self.checkBox_xlsx,
                 self.checkBox_xls, self.checkBox_html, self.checkBox_py,
                 self.checkBox_rar, self.checkBox_png, self.checkBox_jpg,
                 self.checkBox_bmp, self.checkBox_gif, self.checkBox_ico,
                 self.checkBox_flv, self.checkBox_wmv, self.checkBox_avi,
                 self.checkBox_rm, self.checkBox_mp4]
        for box in boxes2:
            if box.isChecked()==True:
                self.filename_extension.append(box.text())
        self.filename_extension = list (set (self.filename_extension))
        print ('houzui:',self.filename_extension)
        edits=[self.lineEdit,self.lineEdit_2,self.lineEdit_3]
        for edit in edits:
            if  edit.text()!='':
                self.keys.append(edit.text())
        self.keys = list (set (self.keys))
        print('keys:',self.keys)

        if len (self.keys) == 0 and len(self.filename_extension)==0:
            QMessageBox.warning (None, '警告', '开始查找前，关键字和后缀不能同时为空！', QMessageBox.Ok)
            return

        self.tarfiles = []

        self.label_displyFindNum.setText ('当前正在查找中,请等待...')
        self.label_displyFindNum.setStyleSheet ("color:red")  # 设置颜色
        self.label_displyFindNum.setFont (QFont ("Timers", 12, QFont.Bold))
        self.label_displyFindNum.repaint ()
        self.textBrowser.clear ()
        self.textBrowser.repaint ()
        self.lineEdit_TargetPath.clear()
        self.lineEdit_TargetPath.repaint()
        if self.label_DisplayCopyStatus.text () != '此处显示文件复制的最终状态':
            self.label_DisplayCopyStatus.setText ('此处显示文件复制的最终状态')
            self.label_DisplayCopyStatus.setFont (QFont ("Timers", 9, QFont.Normal))
            self.label_DisplayCopyStatus.setStyleSheet ("color:black")# 设置颜色
            self.label_DisplayCopyStatus.repaint()
        self.search_File()
        #完成查找后 将相应list清空
        self.paths=[]
        self.keys=[]
        self.filename_extension=[]

    def setCopyPath(self):
        try:
            # 选择复制文件后保存的文件夹路径
            targetPath = QFileDialog.getExistingDirectory (None, "选择待查找文件的可能路径", 'D:\\')
            if os.path.isdir(targetPath):
                self.lineEdit_TargetPath.setText(targetPath)
        except Exception:
            QMessageBox.warning (None, '警告', '请选择一个有效路径……', QMessageBox.Ok)
        else:
            print('targetPath is : {}'.format(targetPath))

    def copyFiles(self):
        if len(self.tarfiles)==0:
            QMessageBox.information(self,'提示','当前查询文件为空，请先查询到文件后再复制文件!', QMessageBox.Close)
            return
        flag=self.is_same_dir ()
        if flag=='Fail':
            return
        else:
            status=myfilesearch.shutil_copy_files(self.tarfiles,self.lineEdit_TargetPath.text())
            # status = myfilesearch.subprocess_copy_files(self.tarfiles,self.lineEdit_TargetPath.text())
            reply=QMessageBox.information(self,'信息','文件复制完成！',QMessageBox.Close)
            if reply==QMessageBox.Close:
                self.label_DisplayCopyStatus.setText (status)
                self.label_DisplayCopyStatus.setStyleSheet ("color:red")# 设置颜色
                self.label_DisplayCopyStatus.setFont(QFont( "Timers" , 12 ,  QFont.Bold))

    def is_same_dir(self):
        for f in self.tarfiles:
            dir, name = os.path.split (f)
            if os.path.samefile(dir,self.lineEdit_TargetPath.text()):
                print('dir:'+dir)
                print('tar:'+self.lineEdit_TargetPath.text())
                QMessageBox.information(None,'提示信息','设置的复制文件夹路径{0}不能和查询文件{1}有相同的文件夹路径，请重新选择'.format(self.lineEdit_TargetPath.text(),f), QMessageBox.Close)
                self.lineEdit_TargetPath.clear()
                self.lineEdit_TargetPath.repaint()
                return 'Fail'
        return 'Pass'