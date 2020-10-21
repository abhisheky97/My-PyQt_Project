from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.setFixedSize(300, 300)
        self.gridLayout = QtWidgets.QGridLayout(Calculator)
        self.gridLayout.setObjectName("gridLayout")
        self.tsquare = QtWidgets.QPushButton(Calculator)
        self.tsquare.setObjectName("tsquare")
        self.gridLayout.addWidget(self.tsquare, 5, 0, 1, 1)
        self.tcube = QtWidgets.QPushButton(Calculator)
        self.tcube.setObjectName("tcube")
        self.gridLayout.addWidget(self.tcube, 5, 1, 1, 1)
        self.t0 = QtWidgets.QPushButton(Calculator)
        self.t0.setObjectName("t0")
        self.gridLayout.addWidget(self.t0, 4, 1, 1, 1)
        self.tclear = QtWidgets.QPushButton(Calculator)
        self.tclear.setObjectName("tclear")
        self.gridLayout.addWidget(self.tclear, 4, 2, 1, 1)
        self.tdiv = QtWidgets.QPushButton(Calculator)
        self.tdiv.setObjectName("tdiv")
        self.gridLayout.addWidget(self.tdiv, 4, 3, 1, 1)
        self.tequals = QtWidgets.QPushButton(Calculator)
        self.tequals.setObjectName("tequals")
        self.gridLayout.addWidget(self.tequals, 4, 0, 1, 1)
        self.tpoint = QtWidgets.QPushButton(Calculator)
        self.tpoint.setObjectName("tpoint")
        self.gridLayout.addWidget(self.tpoint, 5, 2, 1, 1)
        self.tinput = QtWidgets.QLineEdit(Calculator)
        self.tinput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.tinput.setObjectName("tinput")
        self.gridLayout.addWidget(self.tinput, 0, 0, 1, 4)
        self.t3 = QtWidgets.QPushButton(Calculator)
        self.t3.setObjectName("t3")
        self.gridLayout.addWidget(self.t3, 1, 2, 1, 1)
        self.tadd = QtWidgets.QPushButton(Calculator)
        self.tadd.setObjectName("tadd")
        self.gridLayout.addWidget(self.tadd, 1, 3, 1, 1)
        self.t2 = QtWidgets.QPushButton(Calculator)
        self.t2.setObjectName("t2")
        self.gridLayout.addWidget(self.t2, 1, 1, 1, 1)
        self.t4 = QtWidgets.QPushButton(Calculator)
        self.t4.setObjectName("t4")
        self.gridLayout.addWidget(self.t4, 2, 0, 1, 1)
        self.tminus = QtWidgets.QPushButton(Calculator)
        self.tminus.setObjectName("tminus")
        self.gridLayout.addWidget(self.tminus, 2, 3, 1, 1)
        self.t6 = QtWidgets.QPushButton(Calculator)
        self.t6.setObjectName("t6")
        self.gridLayout.addWidget(self.t6, 2, 2, 1, 1)
        self.t7 = QtWidgets.QPushButton(Calculator)
        self.t7.setObjectName("t7")
        self.gridLayout.addWidget(self.t7, 3, 0, 1, 1)
        self.t5 = QtWidgets.QPushButton(Calculator)
        self.t5.setObjectName("t5")
        self.gridLayout.addWidget(self.t5, 2, 1, 1, 1)
        self.t8 = QtWidgets.QPushButton(Calculator)
        self.t8.setObjectName("t8")
        self.gridLayout.addWidget(self.t8, 3, 1, 1, 1)
        self.tmul = QtWidgets.QPushButton(Calculator)
        self.tmul.setObjectName("tmul")
        self.gridLayout.addWidget(self.tmul, 3, 3, 1, 1)
        self.t9 = QtWidgets.QPushButton(Calculator)
        self.t9.setObjectName("t9")
        self.gridLayout.addWidget(self.t9, 3, 2, 1, 1)
        self.t1 = QtWidgets.QPushButton(Calculator)
        self.t1.setObjectName("t1")
        self.gridLayout.addWidget(self.t1, 1, 0, 1, 1)
        self.tdel = QtWidgets.QPushButton(Calculator)
        self.tdel.setObjectName("tdel")
        self.gridLayout.addWidget(self.tdel, 5, 3, 1, 1)

        self.retranslateUi(Calculator)
        self.tclear.clicked.connect(self.tinput.clear)
        QtCore.QMetaObject.connectSlotsByName(Calculator)
 
        self.t0.clicked.connect(self.action0) 
        self.t1.clicked.connect(self.action1) 
        self.t2.clicked.connect(self.action2) 
        self.t3.clicked.connect(self.action3) 
        self.t4.clicked.connect(self.action4) 
        self.t5.clicked.connect(self.action5) 
        self.t6.clicked.connect(self.action6) 
        self.t7.clicked.connect(self.action7) 
        self.t8.clicked.connect(self.action8) 
        self.t9.clicked.connect(self.action9)
        self.tminus.clicked.connect(self.action_minus) 
        self.tequals.clicked.connect(self.action_equal)
        self.tdiv.clicked.connect(self.action_div) 
        self.tmul.clicked.connect(self.action_mul) 
        self.tadd.clicked.connect(self.action_plus) 
        self.tpoint.clicked.connect(self.action_point) 
        self.tdel.clicked.connect(self.action_del)
        self.tsquare.clicked.connect(self.action_square)
        self.tcube.clicked.connect(self.action_cube)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.tsquare.setText(_translate("Calculator", "X^2"))
        self.tcube.setText(_translate("Calculator", "X^3"))
        self.t0.setText(_translate("Calculator", "0"))
        self.t0.setShortcut(_translate("Calculator", "0"))
        self.tclear.setText(_translate("Calculator", "C"))
        self.tdiv.setText(_translate("Calculator", "/"))
        self.tdiv.setShortcut(_translate("Calculator", "/"))
        self.tequals.setText(_translate("Calculator", "="))
        self.tequals.setShortcut(_translate("Calculator", "=, F10"))
        self.tpoint.setText(_translate("Calculator", "."))
        self.tpoint.setShortcut(_translate("Calculator", "."))
        self.t3.setText(_translate("Calculator", "3"))
        self.t3.setShortcut(_translate("Calculator", "3"))
        self.tadd.setText(_translate("Calculator", "+"))
        self.tadd.setShortcut(_translate("Calculator", "+"))
        self.t2.setText(_translate("Calculator", "2"))
        self.t2.setShortcut(_translate("Calculator", "2"))
        self.t4.setText(_translate("Calculator", "4"))
        self.t4.setShortcut(_translate("Calculator", "4"))
        self.tminus.setText(_translate("Calculator", "-"))
        self.tminus.setShortcut(_translate("Calculator", "-"))
        self.t6.setText(_translate("Calculator", "6"))
        self.t6.setShortcut(_translate("Calculator", "6"))
        self.t7.setText(_translate("Calculator", "7"))
        self.t7.setShortcut(_translate("Calculator", "7"))
        self.t5.setText(_translate("Calculator", "5"))
        self.t5.setShortcut(_translate("Calculator", "5"))
        self.t8.setText(_translate("Calculator", "8"))
        self.t8.setShortcut(_translate("Calculator", "8"))
        self.tmul.setText(_translate("Calculator", "*"))
        self.tmul.setShortcut(_translate("Calculator", "*"))
        self.t9.setText(_translate("Calculator", "9"))
        self.t9.setShortcut(_translate("Calculator", "9"))
        self.t1.setText(_translate("Calculator", "1"))
        self.t1.setShortcut(_translate("Calculator", "1"))
        self.tdel.setText(_translate("Calculator", "DEL"))
        self.tdel.setShortcut(_translate("Calculator", "Backspace"))

    def action_plus(self): 
        text = self.tinput.text() 
        self.tinput.setText(text + " + ") 
  
    def action_minus(self):  
        text = self.tinput.text() 
        self.tinput.setText(text + " - ") 
  
    def action_div(self): 
        text = self.tinput.text() 
        self.tinput.setText(text + " / ") 
  
    def action_mul(self): 
        text = self.tinput.text() 
        self.tinput.setText(text + " * ") 
  
    def action_point(self): 
        text = self.tinput.text() 
        self.tinput.setText(text + ".") 
  
    def action0(self): 
        text = self.tinput.text()
        if(text=="0"):
            self.tinput.setText("0")
        else:
            self.tinput.setText(text + "0") 
  
    def action1(self): 
        text = self.tinput.text()
        if(text=="0"):
            self.tinput.setText("1")
        else:
            self.tinput.setText(text + "1")
  
    def action2(self): 
        text = self.tinput.text()
        if(text=="0"):
            self.tinput.setText("2")
        else:
            self.tinput.setText(text + "2") 
  
    def action3(self): 
        text = self.tinput.text()
        if(text=="0"):
            self.tinput.setText("3")
        else:
            self.tinput.setText(text + "3") 
  
    def action4(self): 
        text = self.tinput.text()
        if(text=="0"):
            self.tinput.setText("4")
        else:
            self.tinput.setText(text + "4") 
  
    def action5(self): 
        text = self.tinput.text()
        if(text=="0"):
            self.tinput.setText("5")
        else:
            self.tinput.setText(text + "5") 
  
    def action6(self): 
        text = self.tinput.text()
        if(text=="0"):
            self.tinput.setText("6")
        else:
            self.tinput.setText(text + "6") 
  
    def action7(self): 
        text = self.tinput.text()
        if(text=="0"):
            self.tinput.setText("7")
        else:
            self.tinput.setText(text + "7") 
  
    def action8(self): 
        text = self.tinput.text()
        if(text=="0"):
            self.tinput.setText("8")
        else:
            self.tinput.setText(text + "8") 
  
    def action9(self): 
        text = self.tinput.text()
        if(text=="0"):
            self.tinput.setText("9")
        else:
            self.tinput.setText(text + "9") 
  
    def action_del(self): 
        text = self.tinput.text() 
        print(text[:len(text)-1]) 
        self.tinput.setText(text[:len(text)-1])

    def action_equal(self): 
  
        equation = self.tinput.text() 
  
        try: 
            ans = eval(equation) 
  
            self.tinput.setText(str(ans)) 
  
        except: 
            self.tinput.setText("Wrong Input")

    def action_square(self): 
  
        equation = float(self.tinput.text()) 
  
        try: 
            ans = equation*equation
  
            self.tinput.setText(str(ans)) 
  
        except: 
            self.tinput.setText("Wrong Input")

    def action_cube(self): 
  
        equation = float(self.tinput.text()) 
  
        try: 
            ans = equation*equation*equation
  
            self.tinput.setText(str(ans)) 
  
        except: 
            self.tinput.setText("Wrong Input")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QWidget()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
