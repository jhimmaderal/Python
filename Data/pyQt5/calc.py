from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(333, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outLabel = QtWidgets.QLabel(self.centralwidget)
        self.outLabel.setGeometry(QtCore.QRect(10, 10, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.outLabel.setFont(font)
        self.outLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outLabel.setObjectName("outLabel")

        # Percent
        self.btnPercent = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("%"))
        self.btnPercent.setGeometry(QtCore.QRect(10, 90, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnPercent.setFont(font)
        self.btnPercent.setObjectName("btnPercent")

        # Clear
        self.btnC = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("C"))
        self.btnC.setGeometry(QtCore.QRect(90, 90, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnC.setFont(font)
        self.btnC.setObjectName("btnC")

        # Arrow
        self.btnArrow = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.remove_it())
        self.btnArrow.setGeometry(QtCore.QRect(170, 90, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnArrow.setFont(font)
        self.btnArrow.setObjectName("btnArrow")
        
        # Divide
        self.btnDivide = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("/"))
        self.btnDivide.setGeometry(QtCore.QRect(250, 90, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnDivide.setFont(font)
        self.btnDivide.setObjectName("btnDivide")

        # 8
        self.btnEigth = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("8"))
        self.btnEigth.setGeometry(QtCore.QRect(90, 170, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnEigth.setFont(font)
        self.btnEigth.setObjectName("btnEigth")

        # 7
        self.btnSeven = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("7")) 
        self.btnSeven.setGeometry(QtCore.QRect(10, 170, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnSeven.setFont(font)
        self.btnSeven.setObjectName("btnSeven")

        # 9
        self.btnNine = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("9"))
        self.btnNine.setGeometry(QtCore.QRect(170, 170, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnNine.setFont(font)
        self.btnNine.setObjectName("btnNine")

        # Multiply
        self.btnMultiply = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("X"))
        self.btnMultiply.setGeometry(QtCore.QRect(250, 170, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnMultiply.setFont(font)
        self.btnMultiply.setObjectName("btnMultiply")

        # 5
        self.btnFive = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("5"))
        self.btnFive.setGeometry(QtCore.QRect(90, 250, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnFive.setFont(font)
        self.btnFive.setObjectName("btnFive")

        # 4
        self.btnFour = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("4"))
        self.btnFour.setGeometry(QtCore.QRect(10, 250, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnFour.setFont(font)
        self.btnFour.setObjectName("btnFour")

        # 6
        self.btnSix = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("6"))
        self.btnSix.setGeometry(QtCore.QRect(170, 250, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnSix.setFont(font)
        self.btnSix.setObjectName("btnSix")

        # Minus
        self.btnMinus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("-"))
        self.btnMinus.setGeometry(QtCore.QRect(250, 250, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnMinus.setFont(font)
        self.btnMinus.setObjectName("btnMinus")

        # 2
        self.btnTwo = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("2"))
        self.btnTwo.setGeometry(QtCore.QRect(90, 330, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnTwo.setFont(font)
        self.btnTwo.setObjectName("btnTwo")

        # 1
        self.btnOne = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("1"))
        self.btnOne.setGeometry(QtCore.QRect(10, 330, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnOne.setFont(font)
        self.btnOne.setObjectName("btnOne")

        # 3
        self.btnThree = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("3"))
        self.btnThree.setGeometry(QtCore.QRect(170, 330, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnThree.setFont(font)
        self.btnThree.setObjectName("btnThree")

        # Add
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("+"))
        self.btnAdd.setGeometry(QtCore.QRect(250, 330, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")

        # Decimal
        self.btnDecimal = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.dot_it())
        self.btnDecimal.setGeometry(QtCore.QRect(170, 410, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnDecimal.setFont(font)
        self.btnDecimal.setObjectName("btnDecimal")

        # 0
        self.btnZero = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("0"))
        self.btnZero.setGeometry(QtCore.QRect(90, 410, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnZero.setFont(font)
        self.btnZero.setObjectName("btnZero")

        # AddMinus
        self.btnAddMinus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.plusmini_it())
        self.btnAddMinus.setGeometry(QtCore.QRect(10, 410, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnAddMinus.setFont(font)
        self.btnAddMinus.setObjectName("btnAddMinus")

        # Equal
        self.btnEqual = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("="))
        self.btnEqual.setGeometry(QtCore.QRect(250, 410, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnEqual.setFont(font)
        self.btnEqual.setObjectName("btnEqual")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Remove Character
    def remove_it(self):
        screen = self.outLabel.text()
        screen = screen[:-1]
        self.outLabel.setText(screen)

    # Change Postive to Negativ
    def plusmini_it(self):
        screen = self.outLabel.text()
        if "-" in screen:
            self.outLabel.setText(screen.replace("-", ""))
        else:
            self.outLabel.setText(f"-{screen}")
    
    # Decimal
    def dot_it(self):
        screen = self.outLabel.text()
        
        if screen[-1] == ".":
            pass
        else:
            self.outLabel.setText(f'{screen}.')

    def press_it(self,pressed):
        if pressed == "C":
            self.outLabel.setText("0")
        else:
            if self.outLabel.text () == "0":
                self.outLabel.setText("")
            # Concatinate Prev Value
            self.outLabel.setText(f'{self.outLabel.text()}{pressed}')
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outLabel.setText(_translate("MainWindow", "0"))
        self.btnPercent.setText(_translate("MainWindow", "%"))
        self.btnC.setText(_translate("MainWindow", "C"))
        self.btnArrow.setText(_translate("MainWindow", "<<"))
        self.btnDivide.setText(_translate("MainWindow", "/"))
        self.btnEigth.setText(_translate("MainWindow", "8"))
        self.btnSeven.setText(_translate("MainWindow", "7"))
        self.btnNine.setText(_translate("MainWindow", "9"))
        self.btnMultiply.setText(_translate("MainWindow", "x"))
        self.btnFive.setText(_translate("MainWindow", "5"))
        self.btnFour.setText(_translate("MainWindow", "4"))
        self.btnSix.setText(_translate("MainWindow", "6"))
        self.btnMinus.setText(_translate("MainWindow", "-"))
        self.btnTwo.setText(_translate("MainWindow", "2"))
        self.btnOne.setText(_translate("MainWindow", "1"))
        self.btnThree.setText(_translate("MainWindow", "3"))
        self.btnAdd.setText(_translate("MainWindow", "+"))
        self.btnDecimal.setText(_translate("MainWindow", "."))
        self.btnZero.setText(_translate("MainWindow", "0"))
        self.btnAddMinus.setText(_translate("MainWindow", "+/-"))
        self.btnEqual.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
