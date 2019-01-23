#!/usr/bin/env python3

import sys

import mysql.connector
from mysql.connector import Error

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, 
QTextEdit, QGridLayout, QComboBox, QTableWidget)



class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
	    self.add_wish = QPushButton("Add new wish")
	    self.add_categ = QPushButton("Add new category")
	    self.del_wish = QPushButton("Delete Wish")
	    self.add_categ.clicked.connect(self.add_new_categ)
	    self.add_wish.clicked.connect(self.add_new_wish)
	    self.del_wish.clicked.connect(self.del_wishh)
	    
	    categ = QLabel('Category')
	    listt = QLabel('List of wishes')
	    
	    self.categBox = QComboBox()
	    #self.perem = "Hats"
	    self.categBox.addItems(["Category"])
	    
	    self.categBox.activated[str].connect(self.sqlConnect)
	    
	    self.listtTable = QTableWidget()
	    self.listtTable.setColumnCount(4)
	    self.listtTable.setHorizontalHeaderLabels(["Name", "Price", "Link", "Note"])
		
	    grid = QGridLayout() 
	    grid.setSpacing(10)
	    grid.addWidget(categ, 1, 0)
	    grid.addWidget(self.categBox, 1, 1)
	    grid.addWidget(listt, 3, 1)
	    grid.addWidget(self.listtTable, 4, 0, 1, 5)
	    grid.addWidget(self.add_categ, 5,1)
	    grid.addWidget(self.add_wish, 5,2)
	    grid.addWidget(self.del_wish, 5,3)

	    self.setLayout(grid)
	    self.setGeometry(300, 300, 350, 300)
	    self.setWindowTitle('WishList')
	    self.show()
		
    def categ_sql(self):
	    cnx = mysql.connector.connect(user='user', password='1111',
                              host='127.0.0.1',
                              database='wishlist')
	    try:
	        cursor = cnx.cursor()
	        print('base opened')
	        cursor.execute("""SELECT * FROM categories;""")
	        self.lis = cursor.fetchall()
	        print(lis)
	    except Exception as e:
		    print("******", e)
	    finally:
	        cnx.close()
	        print('base closed')
	        self.categBox.addItems([i[0] for i in self.lis])
	
    def del_wishh(self):
	    self.w3 = DeleteWish()
	    self.w3.catalog_categ_sql()
	    self.w3.show()
    def add_new_categ(self):
	    self.w1 = Add_Categ()
	    self.w1.show()
    def add_new_wish(self):
	    self.w2 = Add_Wish()
	    self.w2.catalog_categ_sql()
	    self.w2.show()
		
    def sqlConnect(self, text):
	    cnx = mysql.connector.connect(user='user', password='1111',
                              host='127.0.0.1',
                              database='wishlist')

	    try:
	        cursor = cnx.cursor()
	        print('base opened')
	        if text == 'Category':
	            cnx.close()
	        else:
	            cursor.execute("""SELECT * FROM """ + text + """;""")
	        
	            result = cursor.fetchall()
	            self.listtTable.setRowCount(0)
			
	            for row_num, row_data in enumerate(result):
	                self.listtTable.insertRow(row_num)
	                for col_num, data in enumerate(row_data):
	                    self.listtTable.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))
	    finally:
	        cnx.close()
	    print('base closed')

class Add_Categ(QWidget):
    def __init__(self):
	    super().__init__()
	    self.show_win()
		
    def show_win(self):
	    self.setWindowTitle('Add_Categ')
	    self.button = QPushButton(self)
	    self.categ = QLabel("Name of category")
	    self.error = QLabel('')
	    self.lineEdit = QLineEdit()
	    self.lineEdit.textChanged[str].connect(self.add_category)
	    grid = QGridLayout()
	    grid.addWidget(self.categ, 1, 1)
	    grid.addWidget(self.lineEdit, 1, 2)
	    grid.addWidget(self.button, 3, 1)
	    grid.addWidget(self.error, 4, 1)
	    self.button.setText('Add')
	    self.setLayout(grid)
	    self.setGeometry(300, 300, 200, 150)
    
    def add_category(self,text):
	    self.per = self.lineEdit.text()
	    self.button.clicked.connect(self.sql_cnt_categ)
	
    def sql_cnt_categ(self):
	    text = self.per
	    cnx = mysql.connector.connect(user='user', password='1111',
                              host='127.0.0.1',
                              database='wishlist')

	    try:
	        cursor = cnx.cursor()
	        print('base opened')
	        cursor.execute("""INSERT INTO categories (category) VALUES ('%s'); """ %text)
	        cursor.execute("""CREATE TABLE %s (name CHAR(10) PRIMARY KEY, price CHAR(7), link CHAR(60), note CHAR(20));""" %text)
	        cnx.commit()
	        print('Added')
	    except Exception as e:
	        print("******", e)
	        self.error.setText('%s already exists' % text)
	        self.error.adjustSize()
	    finally:
	        cnx.close()
	        print('base closed')	
	    
		
class Add_Wish(QWidget):
    def __init__(self):
	    super().__init__()
	    self.show_win()
		
    def show_win(self):
	    self.setWindowTitle('Add_Wish')
	    self.categBox = QComboBox()
	    #self.perem = "Hats"
	    #self.categBox.addItems(["Category"])
	    self.button = QPushButton(self)
	    self.categ = QLabel("Put category")
	    self.wish = QLabel("Name of wish")
	    self.price = QLabel("Price")
	    self.link = QLabel("Link")
	    self.note = QLabel("Note")
	    self.error = QLabel('')
	    #self.lineEdit = QLineEdit()
	    self.wishEdit = QLineEdit()
	    self.priceEdit = QLineEdit()
	    self.linkEdit = QLineEdit()
	    self.noteEdit = QLineEdit()
	    
	    
	    grid = QGridLayout()
	    grid.addWidget(self.categ, 1, 1)
	    grid.addWidget(self.categBox, 1, 2)
	    grid.addWidget(self.wish, 2, 1)
	    grid.addWidget(self.wishEdit, 2, 2)
	    grid.addWidget(self.price, 3, 1)
	    grid.addWidget(self.priceEdit, 3, 2)
	    grid.addWidget(self.link, 4, 1)
	    grid.addWidget(self.linkEdit, 4, 2)
	    grid.addWidget(self.note, 5, 1)
	    grid.addWidget(self.noteEdit, 5, 2)
	    grid.addWidget(self.button, 6, 1)
	    grid.addWidget(self.error, 7, 1)
	    self.button.setText('Add')
	    self.setLayout(grid)
	    self.setGeometry(300, 300, 200, 150)
	    self.categBox.activated[str].connect(self.put_categ)
	    self.wishEdit.textChanged[str].connect(self.write_wish)
	    self.priceEdit.textChanged[str].connect(self.write_price)
	    self.linkEdit.textChanged[str].connect(self.write_link)
	    self.noteEdit.textChanged[str].connect(self.write_note)
	    
	    
    
    def catalog_categ_sql(self):
	    cnx = mysql.connector.connect(user='user', password='1111',
                              host='127.0.0.1',
                              database='wishlist')
	    try:
	        cursor = cnx.cursor()
	        print('base opened')
	        cursor.execute("""SELECT * FROM categories;""")
	        self.lis = cursor.fetchall()
	        print(lis)
	    except Exception as e:
		    print("******", e)
	    finally:
	        cnx.close()
	        print('base closed')
	        self.categBox.addItems([i[0] for i in self.lis])
			
    def put_categ(self, text):
	    self.per1 = text
	    self.button.clicked.connect(self.sql__categ)
    def write_wish(self, text=''):
	    self.per2 = self.wishEdit.text()
    def write_price(self, text=''):
	    self.per3 = self.priceEdit.text()
    def write_link(self, text=''):
	    self.per4 = self.linkEdit.text()
    def write_note(self, text=''):
	    self.per5 = self.noteEdit.text()
	    
		
    def sql__categ(self):
	    text1 = self.per1
	    text2 = self.per2
	    text3 = self.per3
	    text4 = self.per4
	    text5 = self.per5
	    print(text1, text2, text3, text4, text5)
	    cnx = mysql.connector.connect(user='user', password='1111',
                              host='127.0.0.1',
                              database='wishlist')

	    try:
	        cursor = cnx.cursor()
	        print('base opened')
	        cursor.execute("""INSERT INTO %s (name, price, link, note) VALUES ('%s', '%s', '%s', '%s');""" % (text1, text2, text3, text4, text5))
	        cnx.commit()
	        print('Added')
	    except Exception as e:
	        print("******", e)
	        self.error.setText('%s already exists' % text2)
	        self.error.adjustSize()
	    finally:
	        cnx.close()
	        print('base closed')
			
class DeleteWish(QWidget):
    def __init__(self):
	    super().__init__()
	    self.delete_wish()
    
    def delete_wish(self):
	    self.setWindowTitle('Del_Wish')
	    self.categBox = QComboBox()
	    self.button = QPushButton(self)
	    self.categ = QLabel("Put category")
	    self.wish = QLabel("Name of wish")
	    self.wishEdit = QLineEdit()
	    self.error = QLabel('')
	    grid = QGridLayout()
	    grid.addWidget(self.categ, 1, 1)
	    grid.addWidget(self.categBox, 1, 2)
	    grid.addWidget(self.wish, 2, 1)
	    grid.addWidget(self.wishEdit, 2, 2)
	    grid.addWidget(self.button, 6, 1)
	    grid.addWidget(self.error, 7, 1)
	    self.button.setText('Delete')
	    self.setLayout(grid)
	    self.setGeometry(300, 300, 200, 150)
	    self.categBox.activated[str].connect(self.put_categ)
	    self.wishEdit.textChanged[str].connect(self.write_wish)
	    
	    
		
    def catalog_categ_sql(self):
	    cnx = mysql.connector.connect(user='user', password='1111',
                              host='127.0.0.1',
                              database='wishlist')
	    try:
	        cursor = cnx.cursor()
	        print('base opened')
	        cursor.execute("""SELECT * FROM categories;""")
	        self.lis = cursor.fetchall()
	        print(lis)
	    except Exception as e:
		    print("******", e)
	    finally:
	        cnx.close()
	        print('base closed')
	        self.categBox.addItems([i[0] for i in self.lis])
			
    def put_categ(self, text):
	    self.per1 = text
	    self.button.clicked.connect(self.sql__categ)
		
    def write_wish(self, text):
	    self.per2 = self.wishEdit.text()
	    
   
    def sql__categ(self):
	    text1 = self.per1
	    text2 = self.per2
	    print(text1, text2)
	    cnx = mysql.connector.connect(user='user', password='1111',
                              host='127.0.0.1',
                              database='wishlist')

	    try:
	        cursor = cnx.cursor()
	        print('base opened')
	        cursor.execute("""DELETE FROM %s WHERE name = '%s';""" % (text1, text2))
	        cnx.commit()
	        self.error.setText('%s no more' % text2)
	        print('DELETED')
	    except Exception as e:
	        print("******", e)
	        self.error.setText('%s doesnt exist' % text2)
	        self.error.adjustSize()
	    finally:
	        cnx.close()
	        print('base closed')
		
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.categ_sql()
    sys.exit(app.exec_())