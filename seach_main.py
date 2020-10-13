# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seach_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush,QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 592)
        MainWindow.setMaximumSize (QtCore.QSize (797, 592))
        MainWindow.setMinimumSize (QtCore.QSize (797, 592))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon_math01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        # 设置窗体背景
        palette = QtGui.QPalette ()
        # 设置窗体背景自适应
        palette.setBrush (MainWindow.backgroundRole (), QBrush (
            QPixmap ("images/piano.jpg").scaled (
                MainWindow.size (),
                QtCore.Qt.IgnoreAspectRatio,
                QtCore.Qt.SmoothTransformation)))
        MainWindow.setPalette (palette)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_key = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/mango03.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.action_key.setIcon(icon1)
        self.action_key.setObjectName("action_key")
        self.action = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/YC_icon.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.action.setIcon(icon2)
        self.action.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/mango03.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_3.setIcon(icon3)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setIcon(icon)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action_key)
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件处理工具"))
        self.menu.setTitle(_translate("MainWindow", "文件检索"))
        self.menu_2.setTitle(_translate("MainWindow", "使用说明"))
        self.action_key.setText(_translate("MainWindow", "关键字查询"))
        self.action_key.setShortcut(_translate("MainWindow", "Ctrl+K"))
        self.action.setText(_translate("MainWindow", "文件后缀查询"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.action_3.setText(_translate("MainWindow", "综合查询"))
        self.action_3.setShortcut (_translate ("MainWindow", "Ctrl+T"))
        self.action_4.setText(_translate("MainWindow", "详细操作说明"))

