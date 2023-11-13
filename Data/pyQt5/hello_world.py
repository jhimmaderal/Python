from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(427, 539)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.btnClick = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clickMe())
        self.btnClick.setGeometry(QtCore.QRect(20, 140, 371, 101))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        self.btnClick.setFont(font)
        self.btnClick.setObjectName("btnClick")
        
        self.lblHello = QtWidgets.QLabel(self.centralwidget)
        self.lblHello.setGeometry(QtCore.QRect(30, 50, 351, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.lblHello.setFont(font)
        self.lblHello.setObjectName("lblHello")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 427, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Press Button
    def clickMe(self):
        self.lblHello.setText("Boom!")
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnClick.setText(_translate("MainWindow", "Click Me !"))
        self.lblHello.setText(_translate("MainWindow", "Hello World"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
