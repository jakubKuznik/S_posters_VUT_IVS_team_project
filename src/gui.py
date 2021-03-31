from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from sympy import *
from pytexit import py2tex


class Ui_s_cals(object):
    def __init__(self):
        self.content = []
        self.memory = []
        self.result = 0
        self.operators = ['+', '-', '*', '/']
        self.op_on = False

    def setupUi(self, widget):
        # UI components declarations
        self.pushButton_n9 = QtWidgets.QPushButton(widget)
        self.pushButton_n8 = QtWidgets.QPushButton(widget)
        self.pushButton_n7 = QtWidgets.QPushButton(widget)
        self.pushButton_n6 = QtWidgets.QPushButton(widget)
        self.pushButton_n5 = QtWidgets.QPushButton(widget)
        self.pushButton_n4 = QtWidgets.QPushButton(widget)
        self.pushButton_n3 = QtWidgets.QPushButton(widget)
        self.pushButton_n2 = QtWidgets.QPushButton(widget)
        self.pushButton_n1 = QtWidgets.QPushButton(widget)
        self.pushButton_n0 = QtWidgets.QPushButton(widget)
        self.pushButton_smem = QtWidgets.QPushButton(widget)
        self.pushButton_sdot = QtWidgets.QPushButton(widget)
        self.pushButton_s_equal = QtWidgets.QPushButton(widget)
        self.pushButton_smultiply = QtWidgets.QPushButton(widget)
        self.pushButton_sminus = QtWidgets.QPushButton(widget)
        self.pushButton_splus = QtWidgets.QPushButton(widget)
        self.pushButton_left_bracket = QtWidgets.QPushButton(widget)
        self.pushButton_right_bracket = QtWidgets.QPushButton(widget)
        self.pushButton_back = QtWidgets.QPushButton(widget)
        self.pushButton_sdivide = QtWidgets.QPushButton(widget)
        self.pushButton_smemminus = QtWidgets.QPushButton(widget)
        self.pushButton_sqrt = QtWidgets.QPushButton(widget)
        self.pushButton_ssqr = QtWidgets.QPushButton(widget)
        self.pushButton_smemplus = QtWidgets.QPushButton(widget)
        self.pushButton_help = QtWidgets.QPushButton(widget)

        self.pushButton_n9.setGeometry(QtCore.QRect(150, 190, 61, 61))
        self.pushButton_n9.setText("9")

        self.pushButton_n8.setGeometry(QtCore.QRect(80, 190, 61, 61))
        self.pushButton_n8.setText("8")

        self.pushButton_n7.setGeometry(QtCore.QRect(10, 190, 61, 61))
        self.pushButton_n7.setText("7")

        self.pushButton_n6.setGeometry(QtCore.QRect(150, 260, 61, 61))
        self.pushButton_n6.setText("6")

        self.pushButton_n5.setGeometry(QtCore.QRect(80, 260, 61, 61))
        self.pushButton_n5.setText("5")

        self.pushButton_n4.setGeometry(QtCore.QRect(10, 260, 61, 61))
        self.pushButton_n4.setText("4")

        self.pushButton_n3.setGeometry(QtCore.QRect(150, 330, 61, 61))
        self.pushButton_n3.setText("3")

        self.pushButton_n2.setGeometry(QtCore.QRect(80, 330, 61, 61))
        self.pushButton_n2.setText("2")

        self.pushButton_n1.setGeometry(QtCore.QRect(10, 330, 61, 61))
        self.pushButton_n1.setText("1")

        self.pushButton_n0.setGeometry(QtCore.QRect(80, 400, 61, 61))
        self.pushButton_n0.setText("0")

        self.pushButton_smem.setGeometry(QtCore.QRect(10, 400, 61, 61))
        self.pushButton_smem.setAutoFillBackground(False)
        self.pushButton_smem.setText("M")

        self.pushButton_sdot.setGeometry(QtCore.QRect(150, 400, 61, 61))
        self.pushButton_sdot.setAutoFillBackground(False)
        self.pushButton_sdot.setText(",")

        self.pushButton_s_equal.setGeometry(QtCore.QRect(220, 400, 61, 61))
        self.pushButton_s_equal.setAutoFillBackground(False)
        self.pushButton_s_equal.setText("=")

        self.pushButton_smultiply.setGeometry(QtCore.QRect(220, 190, 61, 61))
        self.pushButton_smultiply.setAutoFillBackground(False)
        self.pushButton_smultiply.setText("*")

        self.pushButton_sminus.setGeometry(QtCore.QRect(220, 260, 61, 61))
        self.pushButton_sminus.setAutoFillBackground(False)
        self.pushButton_sminus.setText("-")

        self.pushButton_splus.setGeometry(QtCore.QRect(220, 330, 61, 61))
        self.pushButton_splus.setAutoFillBackground(False)
        self.pushButton_splus.setText("+")

        self.pushButton_left_bracket.setGeometry(QtCore.QRect(10, 140, 61, 41))
        self.pushButton_left_bracket.setAutoFillBackground(False)
        self.pushButton_left_bracket.setText("(")

        self.pushButton_right_bracket.setGeometry(QtCore.QRect(80, 140, 61, 41))
        self.pushButton_right_bracket.setAutoFillBackground(False)
        self.pushButton_right_bracket.setText(")")

        self.pushButton_back.setGeometry(QtCore.QRect(150, 140, 61, 41))
        self.pushButton_back.setAutoFillBackground(False)
        self.pushButton_back.setText("←")

        self.pushButton_sdivide.setGeometry(QtCore.QRect(220, 140, 61, 41))
        self.pushButton_sdivide.setAutoFillBackground(False)
        self.pushButton_sdivide.setText("÷")

        self.pushButton_smemminus.setGeometry(QtCore.QRect(220, 90, 61, 41))
        self.pushButton_smemminus.setAutoFillBackground(False)
        self.pushButton_smemminus.setText("M-")

        self.pushButton_sqrt.setGeometry(QtCore.QRect(80, 90, 61, 41))
        self.pushButton_sqrt.setAutoFillBackground(False)
        self.pushButton_sqrt.setText("√")

        self.pushButton_ssqr.setGeometry(QtCore.QRect(10, 90, 61, 41))
        self.pushButton_ssqr.setAutoFillBackground(False)
        self.pushButton_ssqr.setText("^")

        self.pushButton_smemplus.setGeometry(QtCore.QRect(150, 90, 61, 41))
        self.pushButton_smemplus.setAutoFillBackground(False)
        self.pushButton_smemplus.setText("M+")

        self.pushButton_help.setGeometry(QtCore.QRect(0, 0, 25, 30))
        self.pushButton_help.setText("?")

        QtCore.QMetaObject.connectSlotsByName(widget)

        # Web engine view for latex expressions
        self.view = QWebEngineView(widget)
        self.view.setGeometry(QtCore.QRect(20, 10, 251, 71))
        self.edit = QtWidgets.QLineEdit(widget)
        self.edit.hide()

        widget.setObjectName("widget")
        widget.resize(300, 500)
        widget.setWindowTitle("Abacus")
        # TODO: set fixed size


        QtCore.QMetaObject.connectSlotsByName(widget)
        self.pushButton_n0.clicked.connect(lambda:self.print("0"))
        self.pushButton_n1.clicked.connect(lambda: self.print("1"))
        self.pushButton_n2.clicked.connect(lambda: self.print("2"))
        self.pushButton_n3.clicked.connect(lambda: self.print("3"))
        self.pushButton_n4.clicked.connect(lambda: self.print("4"))
        self.pushButton_n5.clicked.connect(lambda: self.print("5"))
        self.pushButton_n6.clicked.connect(lambda: self.print("6"))
        self.pushButton_n7.clicked.connect(lambda: self.print("7"))
        self.pushButton_n8.clicked.connect(lambda: self.print("8"))
        self.pushButton_n9.clicked.connect(lambda: self.print("9"))
        self.pushButton_back.clicked.connect(self.delete)
        self.pushButton_splus.clicked.connect(lambda: self.print("+"))
        self.pushButton_sminus.clicked.connect(lambda: self.print("-"))
        self.pushButton_smultiply.clicked.connect(lambda: self.print("*"))
        self.pushButton_sdot.clicked.connect(lambda: self.print("."))
        self.pushButton_ssqr.clicked.connect(lambda: self.print("**"))
        self.pushButton_smem.clicked.connect(lambda: self.print("**"))
        self.pushButton_smemplus.clicked.connect(lambda: self.print("**"))
        self.pushButton_smemminus.clicked.connect(lambda: self.print("**"))

    def print(self, command):
        if command in self.operators and self.op_on:
            return
        if self.op_on:
            self.op_on = False
        self.content.append(command)

        if command in self.operators:
            self.content.append('0')
            self.op_on = True
            self.edit.setText(py2tex(''.join(self.content))[2:-3])
            self.content.pop()
        else:
            self.edit.setText(py2tex(''.join(self.content))[2:-2])

        print(self.content)
        # TODO: fix converting strings ending with an operator
        # mozno to spravit iba ako vysvietene tlacitko, program si bude pamatat iba jedno posledne
        # ako na windowsovej kalkulacke a kym sa nestlaci nic za tym, tak sa zatial neprida do content

    def delete(self):
        self.content.pop()
