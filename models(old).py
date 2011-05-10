#-*- coding:utf-8 -*-
#!/usr/bin/python
############################
#Define and Create the Table
import sqlalchemy
from sqlalchemy import *

engine = create_engine('sqlite:///db', echo=True)

metadata = MetaData()
users_table = Table('users', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(12)),
             #Column('email', String),
             Column('password', String(12))
)
metadata.create_all(engine) 
#############################
#Define a Python Class to be Mapped
class User(object):
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

  def __repr__(self):
    return "<User('%s','%s', '%s')>" % (self.name, self.email, self.password)
##############################
#Setting up the Mapping
from sqlalchemy.orm import mapper
mapper(User, users_table) 
########################
#ed_user = User('ed', 'Ed Jones', 'edspassword')
#ed_user.name
#'ed'
#ed_user.password
#'edspassword'
#str(ed_user.id)
#'None'
############################
#Creating a Session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
#######################
#Adding new Objects
#ed_user = User('ed', 'Ed Jones', 'edspassword')
#session.add(ed_user)
#session.commit()
#change password
#ed_user.password = 'f8s7ccs'
#==========================
#session.add_all([
#User('wendy', 'Wendy Williams', 'foobar'),
#     User('mary', 'Mary Contrary', 'xxg527'),
#     User('fred', 'Fred Flinstone', 'blah')])
#session.commit()
################################
#Querying
#for instance in session.query(User).order_by(User.id): 
#  print instance.name, instance.fullname
#for name, fullname in session.query(User.name, User.fullname): 
#  print name, fullname
#===================================
#You can control the names using the label() construct for scalar attributes and aliased for class constructs
#from sqlalchemy.orm import aliased
#user_alias = aliased(User, name='user_alias')
#for row in session.query(user_alias, user_alias.name.label('name_label')).all(): 
#  print row.user_alias, row.name_label
#<User('ed','Ed Jones', 'f8s7ccs')> ed

#########################
#Counting
#session.query(User.id, User.name).filter(User.name.like('%ed')).count() 
#session.query(User.name).group_by(User.name).count()  
