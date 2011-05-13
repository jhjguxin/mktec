# -*- coding:utf-8 -*-
#!/usr/bin/env python
# quitter.py - provide a button to quit this "program"

# Copyright (c) 2010-2011 Algis Kabaila. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public Licence as published
# by the Free Software Foundation, either version 2 of the Licence, or
# version 3 of the Licence, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public Licence for more details.

import sys
import pdb
from PySide.QtGui import *
from PySide.QtCore import *
from PySide import QtGui,QtCore
from ui import Ui_MainWindow
from models import *
from sqlalchemy import desc,asc
from datetime import datetime

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Mktec")
        self.setupUi(self)
##################################################################
        self.article_search_pushButton.clicked.connect(self.searchArticle)
#=========================================
        self.article_tableWidget.selectionBehavior=1
        self.imgfind_pushButton.clicked.connect(self.setOpenFileName)
        #QtCore.QObject.connect(self.imgfind_pushButton, QtCore.SIGNAL("pressed()"), self.setOpenFileName)
        self.update_article_pushButton_2.clicked.connect(self.updateArticle)
        self.delete_article_pushButton.clicked.connect(self.deleteArticle)
        self.article_tableWidget.clicked.connect(self.article_tableWidget_selectionChanged)
        #QtCore.QObject.connect(self.article_tableWidget, QtCore.SIGNAL("self.article_tableWidget.selectionChanged()"), self.article_tableWidget_selectionChanged)
        self.article_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.article_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        

        self.fn=u''
        self.article_tableWidget_query()
        self.article_tableWidget_selectionChanged()

##################################################################
    def searchArticle(self):
        number=int(self.search_article_number_lineEdit.text())
        a=Article.get_by(number=number)
        if a is None:
            self.node.setText(u"No.%d产品没有找到，请检查" % (number))
        else:
            self.article_number_label.setText(unicode(number))
            self.article_name_label.setText(a.name)
            self.article_price_label.setText("%.02f"%(a.price))
            self.imgview1.setPixmap(QtGui.QPixmap(a.image))
            
#=====================================================
    def article_tableWidget_selectionChanged(self):
        print("called article_tableWidget_selectionChanged")
        row=self.article_tableWidget.currentRow()
        #pdb.set_trace()
        if row>=0:
            number = str(self.article_tableWidget.item(row,0).text())
            print(number)
            a = Article.query.filter_by(number=number).one()
            if a is None:
                artSelMsgBox = QMessageBox()
                artSelMsgBox.setText(u"No.%d产品没有找到，请检查" % (number))
                artSelMsgBox.exec_()
            else:
                self.article_number_lineEdit_2.setText(number)
                self.article_name_lineEdit_2.setText(a.name)
                self.article_price_lineEdit_2.setText("%.02f"%(a.price))
                self.article_img_2_lineEdit.setText(a.image)
                self.imgview2.setPixmap(QtGui.QPixmap(a.image))



    def setOpenFileName(self):    
        fileName, filtr = QtGui.QFileDialog.getOpenFileName(self,
                "QFileDialog.getOpenFileName()",
                self.article_img_2_lineEdit.text(),
                "All Files (*);;Text Files (*.txt)")
        if fileName:
            #pdb.set_trace()
            self.article_img_2_lineEdit.setText(fileName)
	    self.imgview2.setPixmap(QtGui.QPixmap(fileName))
	    #self.imgview2.setPixmap(QtGui.QPixmap(r"/home/jhjguxin/Desktop/1_223GXS4.jpg"))
            self.fn=fileName
            self.imgview1.show()
    def updateArticle(self):    
        print ("called updateArticle")
        #upload img
        img = QFileInfo(self.fn)
        imgname=img.fileName()
        QFile.copy(self.fn,u'upload/'+imgname)

        number=int(self.article_number_lineEdit_2.text())
        #pdb.set_trace()
        a=Article.get_by(number=number)
        if a is None:
            name=unicode(self.article_name_lineEdit_2.text())
            price=float(self.article_price_lineEdit_2.text())
            #price=float(self.lineEdit_price.text())
            image=u'upload/'+imgname
            Article(number=number,name=name,image=image,price=price)
            session.commit()
            artAdMsgBox = QMessageBox()
            artAdMsgBox.setText(u"No.%d产品添加成功" % (number))
            artAdMsgBox.exec_()
        else:
            a.number=number
            a.name=unicode(self.article_name_lineEdit_2.text())
            a.price=float(self.article_price_lineEdit_2.text())
            #price=float(self.lineEdit_price.text())
            if imgname:a.image=u'upload/'+imgname
            session.commit()
            artUpMsgBox = QMessageBox()
            artUpMsgBox.setText(u"No.%d产品更新成功" % (number))
            artUpMsgBox.exec_()
        self.article_tableWidget_query()

    def deleteArticle(self):    
        print ("called deleteArticle")
        number=int(self.article_number_lineEdit_2.text())
        a=Article.get_by(number=number)
        if a is None:
            artDeMsgBox = QMessageBox()
            artDeMsgBox.setText(u"没有找到No.%d产品" % (number))
            artDeMsgBox.exec_()
        else:
            a.delete()
            session.commit()
            artDeMsgBox = QMessageBox()
            artDeMsgBox.setText(u"成功删除No.%d产品" % (number))
            artDeMsgBox.exec_()
        self.article_tableWidget_query()


    def article_tableWidget_query(self):
        #pdb.set_trace()
        self.article_tableWidget.clear()
        articles = Article.query.order_by(asc(Article.number)).all()
        self.article_tableWidget.setRowCount(len(articles))
        row_id = 0
        for a in articles:
            item_number = QTableWidgetItem(unicode(a.number))
            #pdb.set_trace()
            item_number.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.article_tableWidget.setItem(row_id,0, item_number)
            
            item_name = QTableWidgetItem(a.name)
            item_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.article_tableWidget.setItem(row_id,1,item_name)
            
            item_price = QTableWidgetItem("%.02f"%(a.price))
            item_price.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.article_tableWidget.setItem(row_id,2, item_price)
            #pdb.set_trace()
            item_created = QTableWidgetItem(u"%d-%d-%d %d:%d"%(a.created.year,a.created.month,a.created.day,a.created.hour,a.created.minute))
            item_created.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.article_tableWidget.setItem(row_id,3, item_created)            
            row_id += 1
 
        self.article_tableWidget.setCurrentItem(self.article_tableWidget.item(0,0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()    
    app.exec_()
