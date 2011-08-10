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
        self.tem_article=[]#example[(article1),(article2),]
        self.trade_article_tableWidget.selectionBehavior=1
        #self.trade_article_tableWidget_query()
        self.trade_article_tableWidget_selectionChanged()
        self.trade_article_tableWidget.clicked.connect(self.trade_article_tableWidget_selectionChanged)
        self.trade_article_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.trade_article_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.clicked=False
        self.article_search_pushButton.clicked.connect(self.searchArticle)
        self.trade_update_pushButton.clicked.connect(self.tradeitem_Update)
        self.trade_clear_pushButton.clicked.connect(self.trade_Clear)
        self.trade_check_pushButton.clicked.connect(self.trade_Check)
        self.trade_save_pushButton.clicked.connect(self.trade_Save)
        self.trade_empty_pushButton.clicked.connect(self.trade_Empty)

#=========================================article_tableWidget
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
#=========================================trade_history_tableWidget
        self.start_dateEdit.setCalendarPopup(True)
        self.start_dateEdit.setDisplayFormat(unicode("yyyy-MM-dd"))
        self.start_dateEdit.setDate(QtCore.QDate.currentDate().addMonths(-1))

        self.end_dateEdit.setCalendarPopup(True)
        self.end_dateEdit.setDisplayFormat(unicode("yyyy-MM-dd"))
        self.end_dateEdit.setDate(QtCore.QDate.currentDate())

        self.search_items=[]
        self.trade_history_fiter=False
        self.trade_history_tableWidget_query()
        self.trade_history_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.trade_history_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.search_trade_pushButton.clicked.connect(self.search_Trade)
        #self.article_tableWidget_selectionChanged()

##################################################################
#=======================================        self.trade_history_tableWidget_query()
    def search_Trade(self):#先查找编号，如果失败则按时间显示
        #pdb.set_trace()
        sdate = self.start_dateEdit.dateTime().toPython()
        edate = self.end_dateEdit.dateTime().addDays(1).toPython()#截止时间到第二天凌晨

        trade_number=self.search_tradenumber_lineEdit.text()


        if not trade_number=="":
            try:
                trade_number=int(trade_number)
                a=Traded_article.query.filter_by(trade_number=trade_number).all()
                self.trade_history_fiter=True
                self.search_items=a
                self.trade_history_tableWidget_query()
            except:
                searchMsgBox = QMessageBox()
                searchMsgBox.setText(u"请输入数字格式的交易编号！下面显示的是按时间检索的结果")
                searchMsgBox.exec_()

                all_traded_article = Traded_article.query.all()
                for a in all_traded_article:
                    if a.created>=sdate and edate>=a.created:
                        self.search_items.append(a)
                if self.search_items!=[]:self.trade_history_fiter=True
                self.trade_history_tableWidget_query()
        else:
            all_traded_article = Traded_article.query.all()
            #pdb.set_trace()
            for a in all_traded_article:
                if a.created>=sdate and edate>=a.created:
                    self.search_items.append(a)
            if self.search_items!=[]:self.trade_history_fiter=True
            self.trade_history_tableWidget_query()

    def trade_history_tableWidget_query(self):
        #pdb.set_trace()
        #self.article_tableWidget.clear()
        counts=0
        totals=0.00
        average_price=0.00
        if not self.trade_history_fiter:
            self.search_items = Traded_article.query.all()
        else:
            pass

        self.trade_history_tableWidget.setRowCount(len(self.search_items))
        row_id = 0
        for a in self.search_items:
            item_number = QTableWidgetItem(unicode(a.number))
            #pdb.set_trace()
            item_number.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.trade_history_tableWidget.setItem(row_id,0, item_number)
            
            item_name = QTableWidgetItem(a.name)
            item_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.trade_history_tableWidget.setItem(row_id,1,item_name)
            
            item_trade_number = QTableWidgetItem(unicode(a.trade_number))
            item_trade_number.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.trade_history_tableWidget.setItem(row_id,2, item_trade_number)

            item_tr_price = QTableWidgetItem("%.02f"%(a.tr_price))
            item_tr_price.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.trade_history_tableWidget.setItem(row_id,3, item_tr_price)

            item_discount = QTableWidgetItem("%.02f"%(a.discount))
            item_discount.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.trade_history_tableWidget.setItem(row_id,4, item_discount)

            item_count = QTableWidgetItem(unicode(a.count))
            item_count.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.trade_history_tableWidget.setItem(row_id,5, item_count)

            counts+=int(a.count)
            totals+=int(a.count)*int(a.tr_price)*float(a.discount)

            item_created = QTableWidgetItem(u"%d-%d-%d %d:%d"%(a.created.year,a.created.month,a.created.day,a.created.hour,a.created.minute))
            item_created.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.trade_history_tableWidget.setItem(row_id,6, item_created)            

            row_id += 1
        if counts!=0:average_price=float(totals)/float(counts)
        self.trade_number_label.setText(unicode(counts))
        self.trade_total_label.setText(u"%0.2f"%(totals))
        self.average_price_label.setText(u"%0.2f"%(average_price))
        self.search_items=[]
        self.trade_article_tableWidget.setCurrentItem(self.article_tableWidget.item(0,0))

#========================================
    def trade_Check(self):
        total=0.0
        if not self.clicked:
            if not self.tem_article==[]:
                for a in self.tem_article:
                    total +=a[2]*a[3]
                try:
                    disc=float(self.trade_discountrate_lineEdit.text())
                    if 0<disc<=1:
                        total=total*disc
                        self.trade_total_label_2.setText("%.02f"%(total))
                        self.clicked=True
                        self.node.setText(u"算帐成功，请付款！")
                    else:
                        self.node.setText(u"请输入0-1之间的折扣率！")
                except:
                    self.node.setText(u"请输入数字！")
            else:
                self.node.setText(u"商品没有添加，请检查")
        else:
            try:
                paied=float(self.trade_payed_lineEdit.text())
                total=float(self.trade_total_label_2.text())
                #pdb.set_trace()
                if paied>=total:
                    self.trade_over_label.setText("%.02f"%(paied-total))
                    self.clicked=False
                    self.node.setText(u"帐已结清，请存档！")
            except:
                self.node.setText(u"请付款！")
    def trade_Save(self):
        disc=float(self.trade_discountrate_lineEdit.text())
        #pdb.set_trace()
        if session.query(Traded_article.trade_number)[:1]==[]:
            trade_number=1
        else:
            trade_number=int(session.query(Traded_article.trade_number)[-1:][0][0])+1
        for a in self.tem_article:
            Traded_article(number=a[0],name=a[1],trade_number=trade_number,tr_price=a[2],discount=disc,count=a[3])
            session.commit()
            self.node.setText(u"交易信息以已保存！")
            self.trade_history_tableWidget_query()
    def trade_article_tableWidget_query(self):
        #pdb.set_trace()
        #self.article_tableWidget.clear()
        self.trade_article_tableWidget.setRowCount(len(self.tem_article))
        row_id = 0
        for a in self.tem_article:
            item_number = QTableWidgetItem(unicode(a[0]))
            #pdb.set_trace()
            item_number.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.trade_article_tableWidget.setItem(row_id,0, item_number)
            
            item_name = QTableWidgetItem(a[1])
            item_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.trade_article_tableWidget.setItem(row_id,1,item_name)
            
            item_tr_price = QTableWidgetItem("%.02f"%(a[2]))
            item_tr_price.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.trade_article_tableWidget.setItem(row_id,2, item_tr_price)

            item_count = QTableWidgetItem("%d"%(a[3]))
            item_count.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.trade_article_tableWidget.setItem(row_id,3, item_count)

            row_id += 1
 
        self.trade_article_tableWidget.setCurrentItem(self.article_tableWidget.item(0,0))


    
    def searchArticle(self):
        print("called searchArticle")
        number=int(self.search_article_number_lineEdit.text())
        a=Article.get_by(number=number)
        if a is None:
            self.node.setText(u"No.%d产品没有找到，请检查" % (number))
        else:
            self.article_number_label.setText(unicode(number))
            self.article_name_label.setText(a.name)
            self.article_price_label.setText("%.02f"%(a.price))
            self.imgview1.setPixmap(QtGui.QPixmap(a.image))

    def tradeitem_Update(self):
        print("called tradeitem_Update")
        number=int(self.article_number_label.text())
        name=unicode(self.article_name_label.text())
        trade_price=unicode(self.re_trade_price_lineEdit.text())
        trade_quantity=unicode(self.trade_quantity_lineEdit.text())
        if number==u"Number":
            self.node.setText(u"还没有指定产品，请检查")
        else:
            if not trade_price==u"":
                try:
                    tr_price=float(trade_price)
                except:
                    self.node.setText(u"交易价格输入不合法，请检查")
            else:
                tr_price=float(self.article_price_label.text())
            if not trade_quantity==u"":
                try:
                    #pdb.set_trace()
                    row=self.trade_article_tableWidget.currentRow()
                    if row >=0:
                        if self.tem_article[row][0]!=0:
                            self.tem_article.remove(self.tem_article[row])#清空以更新

                    count=int(trade_quantity)
                    a=(number,name,tr_price,count)
                    self.tem_article.append(a)
                    print self.tem_article
                    self.node.setText(u"No.%d产品添加/更新成功" %(number))
                    self.article_number_label.setText(u"Number")
                    self.article_name_label.setText(u"name")
                    self.article_price_label.setText(u"0")
                    self.imgview1.setText(u"img")
                    #pdb.set_trace()
                    self.re_trade_price_lineEdit.setText(u"")
                    self.trade_quantity_lineEdit.setText(u"")
                except:
                    self.node.setText(u"交易数目输入不合法，请检查")
            else:
                self.node.setText(u"请输入交易数目，请检查")

        self.trade_article_tableWidget_query()
    def trade_Clear(self):
        try:
            number=int(self.article_number_label.text())
            name=unicode(self.article_name_label.text())
            trade_price=float(self.re_trade_price_lineEdit.text())
            count=int(self.trade_quantity_lineEdit.text())
            a=(number,name,trade_price,count)
            self.tem_article.remove(a)
            self.node.setText(u"No.%d产品删除成功" %(number))
        except:
            self.node.setText(u"删除失败，请重新选择该项商品在试，或是商品未添加")
        self.trade_article_tableWidget_query()
    def trade_Empty(self):
        self.tem_article=[]
        self.trade_total_label_2.setText(u"0.00")
        self.trade_payed_lineEdit.setText(u'0.00')
        self.trade_discountrate_lineEdit.setText(u'1.0')
        self.trade_over_label.setText(u'0.00')
        self.node.setText(u"清除本次所有交易信息！请重新添加！")
        self.trade_article_tableWidget_query()

    def trade_article_tableWidget_selectionChanged(self):
        print("called trade_article_tableWidget_selectionChanged")
        row=self.trade_article_tableWidget.currentRow()
        #pdb.set_trace()
        if row>=0:
            number = int(self.trade_article_tableWidget.item(row,0).text())
            print(number)
            for n in self.tem_article:
                if n[0]==number:
                    a=Article.get_by(number=n[0])
                    #pdb.set_trace()
                    if a is None:
                        self.node.setText(u"No.%d产品在数据库中不存在，请检查" % (n[0]))
                    else:
                        self.article_number_label.setText(unicode(n[0]))
                        self.article_name_label.setText(a.name)
                        self.article_price_label.setText("%.02f"%(a.price))
                        self.imgview1.setPixmap(QtGui.QPixmap(a.image))
                        self.re_trade_price_lineEdit.setText(unicode(n[2]))
                        self.trade_quantity_lineEdit.setText(unicode(n[3]))
                        self.node.setText(u"选中No.%d产品"%a.number)

#=====================================================
    def article_tableWidget_selectionChanged(self):
        print("called article_tableWidget_selectionChanged")
        row=self.article_tableWidget.currentRow()
        #pdb.set_trace()
        if row>=0:
            number = unicode(self.article_tableWidget.item(row,0).text())
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
            if imgname:a.image=unicode(u'upload/'+imgname)
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
        #self.article_tableWidget.clear()
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
