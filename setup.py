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
walk 文件名 #指定光盘信息文件名,使用 "*.cdc"
ini 文件名 #指定光盘信息.ini文件名,使用 "*.ini"
find 关键词 #使用在保存和搜索目录中遍历所有.cdc 文件,输出含有关键词的行
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
"""
  def help_ini(self):
    print '扫描光盘内容 ini cd and export into *.ini'
  def do_ini(self,filename):
    if filename=="":filename = raw_input("输入 ini 文件名:: ")
    print "扫描光盘info保存到:'%s'" % filename
    iniCDinfo(self.CDROM,self.CDDIR+filename)

  def help_dir(self):
    print "指定保存/搜索目录"
  def do_dir(self,pathname):
    if pathname=="": pathname = raw_input("输入指定保存/搜索目录: ")
    default=self.CDDIR
    self.CDDIR=pathname
    print "指定保存/搜索目录:'%s' ;默认是:'%s'" % (self.CDDIR,default)

  def help_find(self):
    print "搜索关键词"
  def do_find(self,keyword):
    if keyword=="":keyword=raw_input("输入搜索关键字: ")
    print "搜索关键词:'%s'" % keyword
    cdcGrep(self.CDDIR,keyword)

if __name__=='__main__':   #this way the module can be
  cdc=PyCDC()              #imported by other programs as well
  cdc.cmdloop()
#  CDROM=os.getcwd()
#  cdWalker(CDROM,'cdc/cdctools.cdc')
"""

import sys,cmd
#测试数据库
if __name__ == '__main__':
  print "创建数据库..."
  setup_all()
  create_all()
  print "启动cmd..."
  mktec=Mktec()
  mktec.cmdloop()

