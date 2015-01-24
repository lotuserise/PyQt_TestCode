# -*- coding:utf-8 -*-
import sys
import sip
sip.setapi('QString', 2)
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication, QLineEdit
# *****************************************************************************
# ダイアログクラス*************************************************************
# *****************************************************************************
MY_DATA = {
    'taro'  : '1990, 01, 01',
    'hanako': '1990, 02, 01',
    'jiro'  : '1990, 03, 01',
    'takako': '1990, 04, 01',
}
 
 
 
class MyDialog( QtGui.QDialog ):
    def __init__( self, parent=None ):
        # 親クラスの初期化。
        super( MyDialog, self ).__init__( parent )
        # ウィンドウ名を設定。
        self.setWindowTitle( 'Tree View Sample' )
        self.index = 0
 
 
        # リストを作成=========================================================
        # QTreeViewを作成。
        self.treeview = QtGui.QTreeView()
        self.treeview.setSortingEnabled( True )     #ソート機能を有効化
        # QTreeViewにコンテキストを追加
        self.treeview.setContextMenuPolicy( QtCore.Qt.CustomContextMenu )
        self.treeview.customContextMenuRequested.connect( self.buildContextMenu )
 
 
        # QStandardItemModel
        self.stdItemModel = QtGui.QStandardItemModel( 0, 2, parent )
        self.stdItemModel.setHeaderData( 0, QtCore.Qt.Horizontal, 'Name' )
        self.stdItemModel.setHeaderData( 1, QtCore.Qt.Horizontal, 'Date' )
 
 
        # QStandardItemModelにアイテムを追加。
        index = 0
        for key in MY_DATA.keys():
            # ローカル８ビットに文字セットを変換してQStandardItemを作成
            nameitem = QtGui.QStandardItem( "test1" )
            dateitem = QtGui.QStandardItem( "test2" )

            dateitem.setEditable( False )
            dateitem.setEditable( False )
 
            self.stdItemModel.setItem( index, 0, nameitem )
            self.stdItemModel.setItem( index, 1, dateitem )
            index += 1
 
        # QTreeViewにmodelをセット。
        self.treeview.setModel( self.stdItemModel ) 
 
        # stdItemModelにシグナルを追加し、self.slotメソッドを接続。
        QtCore.QObject.connect(
            self.treeview.selectionModel(),
            QtCore.SIGNAL('selectionChanged(QItemSelection, QItemSelection)'),
            self.slot
        )
        # =====================================================================
 
 
 
        # レイアウトを定義。===================================================
        layout = QtGui.QHBoxLayout()        #レイアウトを作成。
        layout.addWidget( self.treeview )   #レイアウトにQTreeViewを追加。
        self.setLayout( layout )            #ダイアログにレイアウトをセット。
        # =====================================================================
 
    def slot( self, selected, deselected ):
        for item in selected:
            # セレクトされている各アイテムのインデックスを取得する。
            indexes = item.indexes()
 
            # indexesにはセレクトされた列の各種情報が入っているので、
            # それをfor文で全て取得する。
            textlist = list()
            for index in indexes:
                print( type(index) )
                # 各インデックスのデータを取得
                data = index.data()
                # 取得したデータを文字列に変換して取得
                textlist.append( str(data.toString()) )
            text = ' - '.join( textlist )
            print( text )
 
 
    def buildContextMenu( self, qPoint ):
        # メニューを作成
        menu = QtGui.QMenu( self.treeview )
        menulabels = ['Copy Data', 'Set Data', 'Delete']
        actionlist = []
        for label in menulabels:
            actionlist.append( menu.addAction( label ) )
 
        action = menu.exec_( self.treeview.mapToGlobal( qPoint ) )
        for act in actionlist:
            if act == action:
                print( '  - Menu Label is "%s"' % act.text() )
# *****************************************************************************
# *****************************************************************************
# *****************************************************************************

if __name__ == '__main__':
    app = QtGui.QApplication( sys.argv )
    dialog = MyDialog()
 
    sys.exit( dialog.exec_() ) 