#-*- coding:utf-8 -*-
#!/usr/bin/python

from models import *

def userAdd(u_name,u_password):
  try:
    User(username=u_name,password=u_password)
    session.commit()
    print '创建%s成功'%(u_name)
  except:
    return u"用户创建失败，请检查数据库，或者用户名已存在!"

  print User.query.all()


################################
#Article

