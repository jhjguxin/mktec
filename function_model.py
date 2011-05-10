#-*- coding:utf-8 -*-
#!/usr/bin/python

from models import *

def userAdd(u_name,u_password):
  try:
    User(username=u_name,password=u_password)
    session.commit()
    print User.query.all()
  except:
    return u"用户创建失败，请检查数据库，或者用户名已存在!"

################################
#Article
def browse(self):
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Find Files",
                QtCore.QDir.currentPath())

        if directory:
            if self.directoryComboBox.findText(directory) == -1:
                self.directoryComboBox.addItem(directory)

            self.directoryComboBox.setCurrentIndex(self.directoryComboBox.findText(directory))
def articleAdd():
    do_upload(path)
    assert

def gui
    path = QFileDialog.open
    do_upload(path)
    pass

def do_upload(path)
    pass
