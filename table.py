#!/usr/bin/env python
#coding=utf-8
from PyQt4.QtGui  import *
from PyQt4.QtCore import *  
from PyQt4 import QtGui, QtCore

class MyDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.MyTable = QTableWidget(19,3)
        self.MyTable.setHorizontalHeaderLabels(['SCM1','SCM4','SCM5'])
        self.MyTable.setVerticalHeaderLabels(['Type[Camera]','HostName[Camera]','HostName[LossLess]','HostName[Storage]',
            'Object[CameraServer]','Object[Trigger]','Object[Storage]','EMA[imagesrv]','EMA[lowfilter]','EMA[spectrum]',
            'HostName[ebuilder]','Channel[CameraSelector]','Channel[Trigger]','Interval[Storage]','FilePath[EM]]',
            'FileName[Storage]','Place','DetectorID','StorageFlag'])

        self.resize(1280,680)

        self.MyCombo = QComboBox()
        self.MyCombo.addItem("IMPERX")
        self.MyCombo.addItem("MPCCD")         
        self.MyTable.setCellWidget(0,0,self.MyCombo)

        self.MyCombo = QComboBox()
        self.MyCombo.addItem("IMPERX")
        self.MyCombo.addItem("MPCCD")         
        self.MyTable.setCellWidget(0,1,self.MyCombo)

        #Type[Camera]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("MPCCD")
        self.MyCombo.addItem("IMPERX")         
        self.MyTable.setCellWidget(0,2,self.MyCombo)

        #HostName[Camera]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("xq-bl3-tc-cam01")
        self.MyCombo.addItem("xq-bl3-tc-cam02")
        self.MyCombo.addItem("xq-bl3-tc-cam03")
        self.MyCombo.addItem("xq-bl3-tc-cam03")
        self.MyCombo.addItem("xq-bl3-st1-cam01")
        self.MyCombo.addItem("xq-bl3-st1-cam02")
        self.MyCombo.addItem("xq-bl3-st1-cam03")
        self.MyCombo.addItem("xq-bl3-st2-cam01")
        self.MyCombo.addItem("xq-bl3-st4-cam01")
        self.MyCombo.addItem("xq-bl3-st5-cam01")
        self.MyCombo.addItem("xq-bl3-dh01")
        self.MyCombo.addItem("xq-bl3-dh02")
        self.MyCombo.addItem("xq-bl3-dh03")
        self.MyCombo.addItem("xq-bl3-dh04")
        self.MyCombo.addItem("xq-bl3-dh05")
        self.MyCombo.addItem("xq-bl3-dh06")
        self.MyCombo.addItem("xq-bl3-dh07")
        self.MyCombo.addItem("xq-bl3-dh08")
        self.MyCombo.addItem("xq-bl3-dh09")
        self.MyCombo.addItem("xq-bl3-dh10")
        self.MyCombo.addItem("xq-bl3-dh11")
        self.MyCombo.addItem("xq-bl3-dh12")
        self.MyTable.setCellWidget(1,0,self.MyCombo)

        #HostName[LossLess]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("xq-bl3-ssch-vme-cam01-data")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyTable.setCellWidget(2,0,self.MyCombo)

        #HostName[Storage]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyTable.setCellWidget(3,0,self.MyCombo)

        #Object[CameraServer]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("xfel_bl_3_tc_camsrv_1")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyTable.setCellWidget(4,0,self.MyCombo)
        #HostName[Storage]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("xfel_bl_3_tc_camfpga_1")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyTable.setCellWidget(3,0,self.MyCombo)

        #HostName[Storage]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("xfel_bl_3_tc_cam_selector_stac")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyTable.setCellWidget(5,0,self.MyCombo)

        #HostName[Storage]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("xfel_bl_3_tc_ctdu")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyCombo.addItem("")
        self.MyTable.setCellWidget(6,0,self.MyCombo)

        #HostName[Storage]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("TRUE")
        self.MyCombo.addItem("FALSE")
        self.MyTable.setCellWidget(7,0,self.MyCombo)


        #HostName[Storage]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("TRUE")
        self.MyCombo.addItem("FALSE")
        self.MyTable.setCellWidget(8,0,self.MyCombo)

        #HostName[Storage]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("TRUE")
        self.MyCombo.addItem("FALSE")
        self.MyTable.setCellWidget(9,0,self.MyCombo)


        #HostName[Storage]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("TRUE")
        self.MyCombo.addItem("FALSE")
        self.MyTable.setCellWidget(10,0,self.MyCombo)

        #HostName[Storage]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("1")
        self.MyCombo.addItem("2")
        self.MyCombo.addItem("3")
        self.MyCombo.addItem("4")
        self.MyCombo.addItem("5")
        self.MyCombo.addItem("6")
        self.MyCombo.addItem("7")
        self.MyCombo.addItem("8")
        self.MyCombo.addItem("9")

        self.MyTable.setCellWidget(11,0,self.MyCombo)

        #HostName[Storage]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("1")
        self.MyCombo.addItem("2")
        self.MyCombo.addItem("3")
        self.MyCombo.addItem("4")
        self.MyCombo.addItem("5")
        self.MyCombo.addItem("6")
        self.MyCombo.addItem("7")
        self.MyCombo.addItem("8")
        self.MyCombo.addItem("9")

        self.MyTable.setCellWidget(12,0,self.MyCombo)

        #HostName[Storage]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("2")
        self.MyCombo.addItem("6")
        self.MyTable.setCellWidget(13,0,self.MyCombo)

        #HostName[Storage]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("EH1")
        self.MyCombo.addItem("EH2")
        self.MyCombo.addItem("EH3")
        self.MyCombo.addItem("EH4")
        self.MyTable.setCellWidget(16,0,self.MyCombo)


        #HostName[Storage]
        self.MyCombo = QComboBox()
        self.MyCombo.addItem("TRUE")
        self.MyCombo.addItem("FALSE")

        self.MyTable.setCellWidget(18,0,self.MyCombo)


        newItem = QTableWidgetItem("xq-bl3-tc-cam01-data")
        self.MyTable.setItem(1, 0, newItem)
        newItem = QTableWidgetItem("xq-bl3-st1-cam01-data")
        self.MyTable.setItem(1, 1, newItem)
        newItem = QTableWidgetItem("xq-bl3-st1-cam02-data")
        self.MyTable.setItem(1, 2, newItem) 

        layout = QHBoxLayout()
        layout.addWidget(self.MyTable)
        self.setLayout(layout)    

    def __create_menu(self):
        sele.file_menu = self.menuBar().addMenu("&File")
        loadAction = QtGui.QAction(QtGui.QIcon('icon.png'),'&Load',self)
        loadAction.setStatusTip('Load Config')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myWindow = MyDialog()
    myWindow.show()
    sys.exit(app.exec_()) 
