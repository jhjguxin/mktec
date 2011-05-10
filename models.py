#-*- coding:utf-8 -*-
#!/usr/bin/python
############################
from elixir import *
from datetime import datetime

metadata.bind = "sqlite:///mktec.db"
metadata.bind.echo = True
class User(Entity):
#  user_id = Field(Integer, primary_key=True)
  user_name = Field(Unicode(16), unique=True,required=True)
#  email_address = Field(Unicode(255), unique=True)
  password = Field(Unicode(40))
  user_created = Field(DateTime, default=datetime.now)
  using_options(tablename='tg_user')
    
  def __repr__(self):
    return '<User "%s",created_on:%s>' % (self.user_name, self.user_created)

class Article(Entity):
  "the class of article"
  number = Field(Integer)
  name=Field(Unicode(16))
  image=Field(Unicode(40))
  price=Field(Float)
  created = Field(DateTime, default=datetime.now)
  using_options(tablename='tg_article')
  def __repr__(self):
    return '<Article "%s",created_on:%s>' % (self.name, self.created)
  def save(self,filename,upload='upload'):
    self.image=upload+filename
    super(Article, self).save()

class Traded_article(Entity):
  "the class of article"
  name=Field(Unicode(16))
  discount=Field(Float)
  tr_price=Field(Float)
  created = Field(DateTime, default=datetime.now)
  using_options(tablename='tg_trade')
  def __repr__(self):
    return '<Trade "%s",created_on:%s>' % (self.name, self.created)
if __name__ == '__main__':
  print "创建数据库..."
  setup_all()
  create_all()
