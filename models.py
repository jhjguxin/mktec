#-*- coding:utf-8 -*-
#!/usr/bin/python
############################
from elixir import *
from datetime import datetime
import os

metadata.bind = "sqlite:///mktec.db"
metadata.bind.echo = True
class User(Entity):
#  user_id = Field(Integer, primary_key=True)
  username = Field(Unicode(40), unique=True,required=True)
#  email_address = Field(Unicode(255), unique=True)
  password = Field(Unicode(40))
  user_created = Field(DateTime, default=datetime.now)
  using_options(tablename='tg_user')
    
  def __repr__(self):
    return '<User "%s",created_on:%s>' % (self.username, self.user_created)

class Article(Entity):
  "the class of article"
  number = Field(Integer,unique=True,required=True)
  name=Field(Unicode(16))
  image=Field(Unicode(40))
  price=Field(Float)
  created = Field(DateTime, default=datetime.now)
  using_options(tablename='tg_article')
  def __repr__(self):
    return '<Article "%s",created_on:%s>' % (self.name, self.created)
 # def save(self,filename,upload='upload'):
    #self.image=upload+filename
    #super(Article, self).save()

class Traded_article(Entity):
  "the class of article"
  number= Field(Integer)
  name=Field(Unicode(16))
  trade_number=Field(Integer,default=0)
  tr_price=Field(Float)
  discount=Field(Float)
  count=Field(Integer,default=0)
  created = Field(DateTime, default=datetime.now)
  using_options(tablename='tg_trade')
  def __repr__(self):
    return '<Trade "%s",created_on:%s>' % (self.name, self.created)


setup_all()
if not os.path.exists('mktec.db'):
    create_all()
