# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Editor.ui'
#
# Created: Sat Jan 24 14:27:36 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(384, 214)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.tableWidget = QtGui.QTableWidget(self.centralwidget)
		self.tableWidget.setGeometry(QtCore.QRect(70, 30, 241, 111))
		self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
		self.tableWidget.setColumnCount(2)
		self.tableWidget.setRowCount(2)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(0, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(1, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 384, 24))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		item = self.tableWidget.verticalHeaderItem(0)
		item.setText(_translate("MainWindow", "1", None))
		item = self.tableWidget.verticalHeaderItem(1)
		item.setText(_translate("MainWindow", "2", None))
		item = self.tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Test1", None))
		item = self.tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Test2", None))
		items = [('hoge', 'HOGE'), ('fuga', 'FUGA'), ('piyo', 'PIYO'), ('piyo', 'PIYO')]
		self.tableWidget.clear()
		self.tableWidget.setRowCount(len(items))
		r = 0
		for item in items:
			self.tableWidget.setItem(r, 0, QtGui.QTableWidgetItem(item[0]))
			self.tableWidget.setItem(r, 1, QtGui.QTableWidgetItem(item[1]))
			r += 1

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

