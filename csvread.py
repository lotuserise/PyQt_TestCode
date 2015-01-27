# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'csvread.ui'
#
# Created: Wed Jan 28 04:58:41 2015
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
		MainWindow.resize(734, 438)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.tableWidget = QtGui.QTableWidget(self.centralwidget)
		self.tableWidget.setGeometry(QtCore.QRect(90, 60, 521, 181))
		self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
		self.tableWidget.setColumnCount(5)
		self.tableWidget.setRowCount(5)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(0, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(1, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(2, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(3, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setVerticalHeaderItem(4, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(3, item)
		item = QtGui.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(4, item)
		self.pushButton = QtGui.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(430, 280, 191, 71))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 24))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		for var in range(0,5):
			item = self.tableWidget.verticalHeaderItem(var)
			item.setText(_translate("MainWindow","0", None))
		self.pushButton.setText(_translate("MainWindow", "Read", None))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

