# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Wed Jan 28 02:17:05 2015
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
		MainWindow.resize(856, 688)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.tabWidget = QtGui.QTabWidget(self.centralwidget)
		self.tabWidget.setGeometry(QtCore.QRect(20, 10, 811, 541))
		self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
		self.tabWidget.setIconSize(QtCore.QSize(20, 20))
		self.tabWidget.setDocumentMode(False)
		self.tabWidget.setTabsClosable(False)
		self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
		self.tab = QtGui.QWidget()
		self.tab.setObjectName(_fromUtf8("tab"))
		self.tabWidget.addTab(self.tab, _fromUtf8(""))
		self.tabWidget.setStyleSheet("QTabBar::tab{ height: 30px; width: 100px; }")
		self.tab_2 = QtGui.QWidget()
		self.tab_2.setObjectName(_fromUtf8("tab_2"))
		self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
		self.tab_3 = QtGui.QWidget()
		self.tab_3.setObjectName(_fromUtf8("tab_3"))
		self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
		self.tab_4 = QtGui.QWidget()
		self.tab_4.setObjectName(_fromUtf8("tab_4"))
		self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
		self.tab_5 = QtGui.QWidget()
		self.tab_5.setObjectName(_fromUtf8("tab_5"))
		self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
		self.tab_6 = QtGui.QWidget()
		self.tab_6.setObjectName(_fromUtf8("tab_6"))
		self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
		self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(530, 550, 281, 101))
		self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
		self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.horizontalLayout.addWidget(self.pushButton)
		self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.horizontalLayout.addWidget(self.pushButton_2)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 24))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(3)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "SSCH", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "ST1", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "ST2", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "ST4c", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "ST5", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "ST6", None))
		self.pushButton.setText(_translate("MainWindow", "PushButton", None))
		self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
