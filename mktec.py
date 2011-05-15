# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import os
import pdb
import simplejson

from PySide.QtGui import *
from PySide.QtCore import *
from PySide import QtGui,QtCore

from login import Ui_Login
from main import MainWindow
from models import *


class Login(QMainWindow, Ui_Login):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.pwd_lineEdit.setEchoMode(QtGui.QLineEdit.Password)

        self.login_pushButton.clicked.connect(self.doLogin)
        self.exit_pushButton.clicked.connect(self.doExit)

    def doExit(self):
        print("called doExit")
        self.close()
    
    def doLogin(self):
        print("called doLogin")
        usr=unicode(self.usr_lineEdit.text())
        pwd=unicode(self.pwd_lineEdit.text())
        user=User.get_by(username=usr)
        if user:
            if user.password==pwd:
                self.showMain()
            else:
                loginMsgBox = QMessageBox()
                loginMsgBox.setText(u"密码错误." )
                loginMsgBox.exec_()
        else:
            loginMsgBox = QMessageBox()
            loginMsgBox.setText(u"用户不存在." )
            loginMsgBox.exec_()





    def showMain(self):
        self.main = MainWindow()
        #self.main.showFullScreen()
        self.main.show()
        self.close()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = Login()
    frame.show()    
    app.exec_()
    
