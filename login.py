# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Sun May 15 18:02:09 2011
#      by: pyside-uic 0.2.8 running on PySide 1.0.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(290, 195)
        Login.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtGui.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 120, 181, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.login_pushButton.setObjectName("login_pushButton")
        self.horizontalLayout.addWidget(self.login_pushButton)
        self.exit_pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.horizontalLayout.addWidget(self.exit_pushButton)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 231, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.usr_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.usr_lineEdit.setObjectName("usr_lineEdit")
        self.horizontalLayout_2.addWidget(self.usr_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.pwd_lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.pwd_lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pwd_lineEdit.setObjectName("pwd_lineEdit")
        self.horizontalLayout_3.addWidget(self.pwd_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(QtGui.QApplication.translate("Login", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.login_pushButton.setText(QtGui.QApplication.translate("Login", "登录", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_pushButton.setText(QtGui.QApplication.translate("Login", "退出", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Login", "用户名:", None, QtGui.QApplication.UnicodeUTF8))
        self.usr_lineEdit.setText(QtGui.QApplication.translate("Login", "admin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Login", "密码:", None, QtGui.QApplication.UnicodeUTF8))
        self.pwd_lineEdit.setText(QtGui.QApplication.translate("Login", "admin", None, QtGui.QApplication.UnicodeUTF8))

