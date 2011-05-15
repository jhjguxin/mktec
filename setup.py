# -*- coding: utf-8 -*-
#db_setup.py
import sys,cmd,pdb
from models import *
from function_model import *
class Mktec(cmd.Cmd):
  def __init__(self):
    cmd.Cmd.__init__(self)#initialize the base class
    self.upload='upload'
    self.prompt='(Mktec)>'
    self.intro='''Mktec dbsetup 使用说明:
useradd 创建用户 #create admin user
?           #查询
EOF        # 退出系统,也可以使用 Crtl+D(Unix)|Ctrl+Z(Dos/Windows)
'''

  def help_EOF(self):
    print '退出程序 Quits the program'
  def do_EOF(self,line):
    sys.exit()

  def help_useradd(self):
    print '创建管理员用户...'
  #pdb.set_trace()
  def do_useradd(self,line):
    print line
    username = raw_input("输入帐号:: ")
    password = raw_input("密码:: ")
    print "创建用户:'%s'" % username
    print userAdd(username,password)

import sys,cmd
#测试数据库
if __name__ == '__main__':
  print "创建数据库..."
  setup_all()
  create_all()
  print "启动cmd..."
  mktec=Mktec()
  mktec.cmdloop()

