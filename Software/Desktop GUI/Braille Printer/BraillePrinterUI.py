# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_BraillePrinter(object):
    def setupUi(self, BraillePrinter):
        BraillePrinter.setObjectName(_fromUtf8("BraillePrinter"))
        BraillePrinter.setWindowModality(QtCore.Qt.NonModal)
        #BraillePrinter.resize(900, 450)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BraillePrinter.sizePolicy().hasHeightForWidth())
        BraillePrinter.setSizePolicy(sizePolicy)
        BraillePrinter.setMinimumSize(QtCore.QSize(900, 450))
        BraillePrinter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Img/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        BraillePrinter.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(BraillePrinter)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ToolBar = QtGui.QGridLayout()
        self.ToolBar.setObjectName(_fromUtf8("ToolBar"))
        self.horizontalLayoutToolBar = QtGui.QHBoxLayout()
        self.horizontalLayoutToolBar.setObjectName(_fromUtf8("horizontalLayoutToolBar"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutToolBar.addItem(spacerItem)
        # self.FullScreenCheckBox = QtGui.QCheckBox(self.centralwidget)
        # self.FullScreenCheckBox.setObjectName(_fromUtf8("FullScreenCheckBox"))
        #self.horizontalLayoutToolBar.addWidget(self.FullScreenCheckBox)
        self.ToolBar.addLayout(self.horizontalLayoutToolBar, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.ToolBar)
        self.TextArea = QtGui.QGridLayout()
        self.TextArea.setObjectName(_fromUtf8("TextArea"))
        self.TextEditer = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextEditer.sizePolicy().hasHeightForWidth())
        self.TextEditer.setSizePolicy(sizePolicy)
        self.TextEditer.setMinimumSize(QtCore.QSize(0, 0))
        self.TextEditer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.TextEditer.setObjectName(_fromUtf8("TextEditer"))
        self.TextEditer.setReadOnly(True)
        self.TextArea.addWidget(self.TextEditer, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.TextArea)
        self.ButtonArea = QtGui.QGridLayout()
        self.ButtonArea.setObjectName(_fromUtf8("ButtonArea"))
        self.horizontalLayoutForButtonArea = QtGui.QHBoxLayout()
        self.horizontalLayoutForButtonArea.setObjectName(_fromUtf8("horizontalLayoutForButtonArea"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutForButtonArea.addItem(spacerItem1)
        self.Print = QtGui.QPushButton(self.centralwidget)
        self.Print.setObjectName(_fromUtf8("Print"))
        self.horizontalLayoutForButtonArea.addWidget(self.Print)
        self.Cancel = QtGui.QPushButton(self.centralwidget)
        self.Cancel.setObjectName(_fromUtf8("Cancel"))
        self.horizontalLayoutForButtonArea.addWidget(self.Cancel)
        self.ButtonArea.addLayout(self.horizontalLayoutForButtonArea, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.ButtonArea)
        self.ProgressBar = QtGui.QGridLayout()
        self.ProgressBar.setObjectName(_fromUtf8("ProgressBar"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.ProgressBar.addWidget(self.progressBar, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.ProgressBar)
        BraillePrinter.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BraillePrinter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        BraillePrinter.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(BraillePrinter)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BraillePrinter.setStatusBar(self.statusbar)
        self.actionOpen_File = QtGui.QAction(BraillePrinter)
        self.actionOpen_File.setObjectName(_fromUtf8("actionOpen_File"))
        self.actionPrint_File = QtGui.QAction(BraillePrinter)
        self.actionPrint_File.setObjectName(_fromUtf8("actionPrint_File"))
        self.actionExit = QtGui.QAction(BraillePrinter)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionChange_Color = QtGui.QAction(BraillePrinter)
        self.actionChange_Color.setObjectName(_fromUtf8("actionChange_Color"))
        self.actionChange_Font = QtGui.QAction(BraillePrinter)
        self.actionChange_Font.setObjectName(_fromUtf8("actionChange_Font"))
        self.actionChange_Text_Color = QtGui.QAction(BraillePrinter)
        self.actionChange_Text_Color.setObjectName(_fromUtf8("actionChange_Text_Color"))
        self.actionFull_Screen = QtGui.QAction(BraillePrinter)
        self.actionFull_Screen.setObjectName(_fromUtf8("actionFull_Screen"))
        self.actionHelp = QtGui.QAction(BraillePrinter)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionAbout = QtGui.QAction(BraillePrinter)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSetting.addAction(self.actionChange_Color)
        self.menuSetting.addAction(self.actionChange_Font)
        self.menuSetting.addAction(self.actionChange_Text_Color)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.actionFull_Screen)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(BraillePrinter)
        QtCore.QMetaObject.connectSlotsByName(BraillePrinter)

    def retranslateUi(self, BraillePrinter):
        BraillePrinter.setWindowTitle(_translate("BraillePrinter", "Braille Printer", None))
        #self.FullScreenCheckBox.setText(_translate("BraillePrinter", "Full Screen", None))
        self.Print.setText(_translate("BraillePrinter", "Print", None))
        self.Cancel.setText(_translate("BraillePrinter", "Cancel", None))
        self.menuFile.setTitle(_translate("BraillePrinter", "File", None))
        self.menuSetting.setTitle(_translate("BraillePrinter", "Window", None))
        self.menuHelp.setTitle(_translate("BraillePrinter", "Help", None))
        self.actionOpen_File.setText(_translate("BraillePrinter", "Open File", None))
        self.actionOpen_File.setShortcut(_translate("BraillePrinter", "Ctrl+O", None))
        self.actionPrint_File.setText(_translate("BraillePrinter", "Print File", None))
        self.actionPrint_File.setShortcut(_translate("BraillePrinter", "Ctrl+P", None))
        self.actionExit.setText(_translate("BraillePrinter", "Exit", None))
        self.actionExit.setShortcut(_translate("BraillePrinter", "Ctrl+Q", None))
        self.actionChange_Color.setText(_translate("BraillePrinter", "Change Color", None))
        self.actionChange_Color.setShortcut(_translate("BraillePrinter", "Alt+C", None))
        self.actionChange_Font.setText(_translate("BraillePrinter", "Change Font", None))
        self.actionChange_Font.setShortcut(_translate("BraillePrinter", "Alt+F", None))
        self.actionChange_Text_Color.setText(_translate("BraillePrinter", "Change Text Color", None))
        self.actionChange_Text_Color.setShortcut(_translate("BraillePrinter", "Alt+S", None))
        self.actionFull_Screen.setText(_translate("BraillePrinter", "Full Screen", None))
        self.actionFull_Screen.setShortcut(_translate("BraillePrinter", "F11", None))
        self.actionHelp.setText(_translate("BraillePrinter", "Help", None))
        self.actionHelp.setShortcut(_translate("BraillePrinter", "F1", None))
        self.actionAbout.setText(_translate("BraillePrinter", "About", None))
        self.actionAbout.setShortcut(_translate("BraillePrinter", "F12", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BraillePrinter = QtGui.QMainWindow()
    ui = Ui_BraillePrinter()
    ui.setupUi(BraillePrinter)
    BraillePrinter.show()
    sys.exit(app.exec_())

