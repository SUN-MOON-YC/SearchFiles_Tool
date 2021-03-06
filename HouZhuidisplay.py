# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ZHdisplay.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QBrush
import os
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 604)
        MainWindow.setMaximumSize (QtCore.QSize (720, 604))
        MainWindow.setMinimumSize (QtCore.QSize (720, 604))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/YC_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        # 设置窗体背景
        palette = QtGui.QPalette ()
        # 设置窗体背景自适应
        palette.setBrush (MainWindow.backgroundRole (), QBrush (
            QPixmap ("images/snow.jpg").scaled (
                MainWindow.size (),
                QtCore.Qt.IgnoreAspectRatio,
                QtCore.Qt.SmoothTransformation)))
        MainWindow.setPalette (palette)
        MainWindow.setAutoFillBackground (True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_sourcePath = QtWidgets.QLabel(self.centralwidget)
        self.label_sourcePath.setGeometry(QtCore.QRect(90, 10, 171, 16))
        self.label_sourcePath.setObjectName("label_sourcePath")
        self.lineEdit_sourcePath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sourcePath.setGeometry(QtCore.QRect(230, 10, 291, 20))
        self.lineEdit_sourcePath.setObjectName("lineEdit_sourcePath")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 30, 291, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_C = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_C.setObjectName("checkBox_C")
        self.horizontalLayout.addWidget(self.checkBox_C)
        self.checkBox_D = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_D.setObjectName("checkBox_D")
        self.horizontalLayout.addWidget(self.checkBox_D)
        self.checkBox_E = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_E.setObjectName("checkBox_E")
        self.horizontalLayout.addWidget(self.checkBox_E)
        self.pushButton_selectSourcePath = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_selectSourcePath.setGeometry(QtCore.QRect(550, 10, 75, 23))
        self.pushButton_selectSourcePath.setObjectName("pushButton_selectSourcePath")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 171, 16))
        self.label_2.setObjectName("label_2")
        self.checkBox_pdf = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_pdf.setGeometry(QtCore.QRect(160, 130, 71, 16))
        self.checkBox_pdf.setObjectName("checkBox_pdf")
        self.checkBox_txt = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_txt.setGeometry(QtCore.QRect(260, 130, 71, 16))
        self.checkBox_txt.setObjectName("checkBox_txt")
        self.checkBox_doc = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_doc.setGeometry(QtCore.QRect(360, 130, 71, 16))
        self.checkBox_doc.setObjectName("checkBox_doc")
        self.checkBox_docx = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_docx.setGeometry(QtCore.QRect(470, 130, 71, 16))
        self.checkBox_docx.setObjectName("checkBox_docx")
        self.checkBox_csv = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_csv.setGeometry(QtCore.QRect(570, 130, 71, 16))
        self.checkBox_csv.setObjectName("checkBox_csv")
        self.checkBox_xlsx = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_xlsx.setGeometry(QtCore.QRect(160, 150, 71, 16))
        self.checkBox_xlsx.setObjectName("checkBox_xlsx")
        self.checkBox_xls = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_xls.setGeometry(QtCore.QRect(260, 150, 71, 16))
        self.checkBox_xls.setObjectName("checkBox_xls")
        self.checkBox_html = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_html.setGeometry(QtCore.QRect(360, 150, 71, 16))
        self.checkBox_html.setObjectName("checkBox_html")
        self.checkBox_py = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_py.setGeometry(QtCore.QRect(470, 150, 71, 16))
        self.checkBox_py.setObjectName("checkBox_py")
        self.checkBox_rar = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_rar.setGeometry(QtCore.QRect(570, 150, 71, 16))
        self.checkBox_rar.setObjectName("checkBox_rar")
        self.checkBox_png = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_png.setGeometry(QtCore.QRect(160, 170, 71, 16))
        self.checkBox_png.setObjectName("checkBox_png")
        self.checkBox_jpg = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_jpg.setGeometry(QtCore.QRect(260, 170, 71, 16))
        self.checkBox_jpg.setObjectName("checkBox_jpg")
        self.checkBox_bmp = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_bmp.setGeometry(QtCore.QRect(360, 170, 71, 16))
        self.checkBox_bmp.setObjectName("checkBox_bmp")
        self.checkBox_gif = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_gif.setGeometry(QtCore.QRect(470, 170, 71, 16))
        self.checkBox_gif.setObjectName("checkBox_gif")
        self.checkBox_ico = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_ico.setGeometry(QtCore.QRect(570, 170, 71, 16))
        self.checkBox_ico.setObjectName("checkBox_ico")
        self.label_displyFindNum = QtWidgets.QLabel(self.centralwidget)
        self.label_displyFindNum.setGeometry(QtCore.QRect(260, 250, 181, 16))
        self.label_displyFindNum.setObjectName("label_displyFindNum")
        self.lineEdit_TargetPath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_TargetPath.setGeometry(QtCore.QRect(220, 490, 291, 20))
        self.lineEdit_TargetPath.setObjectName("lineEdit_TargetPath")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 490, 171, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_selectTargetPath = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_selectTargetPath.setGeometry(QtCore.QRect(540, 490, 75, 23))
        self.pushButton_selectTargetPath.setObjectName("pushButton_selectTargetPath")
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setGeometry(QtCore.QRect(100, 250, 75, 23))
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_copy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copy.setGeometry(QtCore.QRect(90, 530, 75, 23))
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.checkBox_flv = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_flv.setGeometry(QtCore.QRect(570, 190, 71, 16))
        self.checkBox_flv.setObjectName("checkBox_flv")
        self.checkBox_wmv = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_wmv.setGeometry(QtCore.QRect(160, 190, 71, 16))
        self.checkBox_wmv.setObjectName("checkBox_wmv")
        self.checkBox_avi = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_avi.setGeometry(QtCore.QRect(360, 190, 71, 16))
        self.checkBox_avi.setObjectName("checkBox_avi")
        self.checkBox_rm = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_rm.setGeometry(QtCore.QRect(470, 190, 71, 16))
        self.checkBox_rm.setObjectName("checkBox_rm")
        self.checkBox_mp4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_mp4.setGeometry(QtCore.QRect(260, 190, 71, 16))
        self.checkBox_mp4.setObjectName("checkBox_mp4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 220, 171, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_CustomerDefineHZ = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_CustomerDefineHZ.setGeometry(QtCore.QRect(330, 220, 291, 20))
        self.lineEdit_CustomerDefineHZ.setObjectName("lineEdit_CustomerDefineHZ")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(90, 280, 561, 201))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 559, 199))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 561, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_DisplayCopyStatus = QtWidgets.QLabel(self.centralwidget)
        self.label_DisplayCopyStatus.setGeometry(QtCore.QRect(220, 530, 181, 16))
        self.label_DisplayCopyStatus.setObjectName("label_DisplayCopyStatus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "指定文件后缀进行查询"))
        self.label_sourcePath.setText(_translate("MainWindow", "文件可能存放的路径："))
        self.checkBox_C.setText(_translate("MainWindow", "C:/"))
        self.checkBox_D.setText(_translate("MainWindow", "D:/"))
        self.checkBox_E.setText(_translate("MainWindow", "E:/"))
        self.pushButton_selectSourcePath.setText(_translate("MainWindow", "浏览"))
        self.label_2.setText(_translate("MainWindow", "文件的后缀(忽略大小写)："))
        self.checkBox_pdf.setText(_translate("MainWindow", ".pdf"))
        self.checkBox_txt.setText(_translate("MainWindow", ".txt"))
        self.checkBox_doc.setText(_translate("MainWindow", ".doc"))
        self.checkBox_docx.setText(_translate("MainWindow", ".docx"))
        self.checkBox_csv.setText(_translate("MainWindow", ".csv"))
        self.checkBox_xlsx.setText(_translate("MainWindow", ".xlsx"))
        self.checkBox_xls.setText(_translate("MainWindow", ".xls"))
        self.checkBox_html.setText(_translate("MainWindow", ".html"))
        self.checkBox_py.setText(_translate("MainWindow", ".py"))
        self.checkBox_rar.setText(_translate("MainWindow", ".rar"))
        self.checkBox_png.setText(_translate("MainWindow", ".png"))
        self.checkBox_jpg.setText(_translate("MainWindow", ".jpg"))
        self.checkBox_bmp.setText(_translate("MainWindow", ".bmp"))
        self.checkBox_gif.setText(_translate("MainWindow", ".gif"))
        self.checkBox_ico.setText(_translate("MainWindow", ".ico"))
        self.label_displyFindNum.setText(_translate("MainWindow", "此处显示查找到文件的数量"))
        self.label_4.setText(_translate("MainWindow", "复制文件到指定文件夹："))
        self.pushButton_selectTargetPath.setText(_translate("MainWindow", "选择"))
        self.pushButton_search.setText(_translate("MainWindow", "开始查找"))
        self.pushButton_copy.setText(_translate("MainWindow", "开始复制"))
        self.checkBox_flv.setText(_translate("MainWindow", ".flv"))
        self.checkBox_wmv.setText(_translate("MainWindow", ".wmv"))
        self.checkBox_avi.setText(_translate("MainWindow", ".avi"))
        self.checkBox_rm.setText(_translate("MainWindow", ".rm"))
        self.checkBox_mp4.setText(_translate("MainWindow", ".mp4"))
        self.label_5.setText(_translate("MainWindow", "自定义文件的后缀(忽略大小写)：："))
        self.label_DisplayCopyStatus.setText(_translate("MainWindow", "此处显示文件复制的最终状态"))
