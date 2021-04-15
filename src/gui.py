from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton


class App(QWidget):
    def __init__(self, ):
        super().__init__()
        self.content = []
        self.memory = []
        self.result = 0
        self.operators = ['+', '-', '*', '/']
        self.setFixedSize(290, 400)
        # TODO: icon

        # UI ELEMENTS
        self.pushButton_n9 = QPushButton(self)
        self.pushButton_n8 = QPushButton(self)
        self.pushButton_n7 = QPushButton(self)
        self.pushButton_n6 = QPushButton(self)
        self.pushButton_n5 = QPushButton(self)
        self.pushButton_n4 = QPushButton(self)
        self.pushButton_n3 = QPushButton(self)
        self.pushButton_n2 = QPushButton(self)
        self.pushButton_n1 = QPushButton(self)
        self.pushButton_n0 = QPushButton(self)
        self.pushButton_smem = QPushButton(self)
        self.pushButton_sdot = QPushButton(self)
        self.pushButton_s_equal = QPushButton(self)
        self.pushButton_smultiply = QPushButton(self)
        self.pushButton_sminus = QPushButton(self)
        self.pushButton_splus = QPushButton(self)
        self.pushButton_left_bracket = QtWidgets.QPushButton(self)
        self.pushButton_right_bracket = QtWidgets.QPushButton(self)
        self.pushButton_back = QtWidgets.QPushButton(self)
        self.pushButton_sdivide = QtWidgets.QPushButton(self)
        self.pushButton_smemminus = QtWidgets.QPushButton(self)
        self.pushButton_sqrt = QtWidgets.QPushButton(self)
        self.pushButton_ssqr = QtWidgets.QPushButton(self)
        self.pushButton_smemplus = QtWidgets.QPushButton(self)
        self.pushButton_help = QtWidgets.QPushButton(self)
        self.output1 = QtWidgets.QLabel(self)
        self.output2 = QtWidgets.QLabel(self)

        self.setup_ui()

    def setup_ui(self):
        self.resize(300, 500)
        self.setWindowTitle("Imposter Calculator")

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

        self.output1.setGeometry(QtCore.QRect(20, 10, 251, 40))
        self.output1.setFont(QFont('Comic Sans MS', 15))
        self.output1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.output2.setGeometry(QtCore.QRect(20, 41, 251, 71))
        self.output2.setFont(QFont('Comic Sans MS', 20))

        self.pushButton_n0.clicked.connect(lambda: self.print("0"))
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

    def change(self, command):
        self.content.append(command)

    def print(self, number):
        self.content.append(number)
        print(self.content)
        self.output1.setText(''.join(self.content))
        temp = ''.join(self.content)
        try:
            temp = eval(temp)
            self.output2.setText(str(temp))
        except SyntaxError:
            pass

    def delete(self):
        if len(self.content) != 0:
            self.content.pop()
            print(self.content)
            self.output1.setText(''.join(self.content))
            temp = ''.join(self.content)
            try:
                temp = eval(temp)
                self.output2.setText(str(temp))
            except SyntaxError:
                pass
            if len(self.content) == 0:
                self.output2.setText('')