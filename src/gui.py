from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox


class App(QWidget):
    def __init__(self, ):
        super().__init__()
        self.content = ['0']
        self.memory = '0'
        self.displayed_content = ['0']
        self.result = 0
        self.operators = ['+', '-', '*', '/', '**0.5', '.']
        self.numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.setFixedSize(290, 480)
        # TODO: icon

        # UI ELEMENTS

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

        self.list_of_buttons = []

        self.digit_buttons = [["0", [80, 400, 61, 61]],
                              ["1", [10, 330, 61, 61]],
                              ["2", [80, 330, 61, 61]],
                              ["3", [150, 330, 61, 61]],
                              ["4", [10, 260, 61, 61]],
                              ["5", [80, 260, 61, 61]],
                              ["6", [150, 260, 61, 61]],
                              ["7", [10, 190, 61, 61]],
                              ["8", [80, 190, 61, 61]],
                              ["9", [150, 190, 61, 61]]]

        self.setup_ui()

    @staticmethod
    def show_dialog():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return_value = msg.exec_()
        print("value of pressed message box button:", return_value)

    def setup_ui(self):
        self.resize(300, 500)
        self.setWindowTitle("Imposter Calculator")

        for i in range(10):
            x_coord = self.digit_buttons[i][1][0]
            y_coord = self.digit_buttons[i][1][1]
            text = self.digit_buttons[i][0]
            size = 61
            button = QPushButton(self.digit_buttons[i][0], self)
            button.setGeometry(QtCore.QRect(x_coord, y_coord, size, size))
            button.clicked.connect(lambda: self.print(text, text))

        self.pushButton_smem.setGeometry(QtCore.QRect(10, 400, 61, 61))
        self.pushButton_smem.setText("M")

        self.pushButton_sdot.setGeometry(QtCore.QRect(150, 400, 61, 61))
        self.pushButton_sdot.setText(",")

        self.pushButton_s_equal.setGeometry(QtCore.QRect(220, 400, 61, 61))
        self.pushButton_s_equal.setText("=")

        self.pushButton_smultiply.setGeometry(QtCore.QRect(220, 190, 61, 61))
        self.pushButton_smultiply.setText("*")

        self.pushButton_sminus.setGeometry(QtCore.QRect(220, 260, 61, 61))
        self.pushButton_sminus.setText("-")

        self.pushButton_splus.setGeometry(QtCore.QRect(220, 330, 61, 61))
        self.pushButton_splus.setText("+")

        self.pushButton_left_bracket.setGeometry(QtCore.QRect(10, 140, 61, 41))
        self.pushButton_left_bracket.setText("(")

        self.pushButton_right_bracket.setGeometry(QtCore.QRect(80, 140, 61, 41))
        self.pushButton_right_bracket.setText(")")

        self.pushButton_back.setGeometry(QtCore.QRect(150, 140, 61, 41))
        self.pushButton_back.setText("←")

        self.pushButton_sdivide.setGeometry(QtCore.QRect(220, 140, 61, 41))
        self.pushButton_sdivide.setText("÷")

        self.pushButton_smemminus.setGeometry(QtCore.QRect(220, 90, 61, 41))
        self.pushButton_smemminus.setText("M-")

        self.pushButton_sqrt.setGeometry(QtCore.QRect(80, 90, 61, 41))
        self.pushButton_sqrt.setText("[2]√")

        self.pushButton_ssqr.setGeometry(QtCore.QRect(10, 90, 61, 41))
        self.pushButton_ssqr.setText("^")

        self.pushButton_smemplus.setGeometry(QtCore.QRect(150, 90, 61, 41))
        self.pushButton_smemplus.setText("M+")

        self.pushButton_help.setGeometry(QtCore.QRect(0, 0, 35, 35))
        self.pushButton_help.setText("?")

        self.output1.setGeometry(QtCore.QRect(20, 10, 251, 40))
        self.output1.setFont(QFont('Comic Sans MS', 15))
        self.output1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.output2.setGeometry(QtCore.QRect(20, 41, 251, 71))
        self.output2.setFont(QFont('Comic Sans MS', 20))

        self.pushButton_back.clicked.connect(self.delete)
        self.pushButton_splus.clicked.connect(lambda: self.print("+", "+"))
        self.pushButton_sminus.clicked.connect(lambda: self.print("-", "-"))
        self.pushButton_smultiply.clicked.connect(lambda: self.print("*", "*"))
        self.pushButton_sdot.clicked.connect(lambda: self.print(".", "."))
        self.pushButton_ssqr.clicked.connect(lambda: self.print("**", "^"))
        self.pushButton_sqrt.clicked.connect(lambda: self.print("**0.5", "[2]√"))
        self.pushButton_sdivide.clicked.connect(lambda: self.print("/", "/"))
        self.pushButton_smem.clicked.connect(lambda: self.print(self.memory, "M"))
        self.pushButton_smemplus.clicked.connect(self.add_to_memory)
        self.pushButton_smemminus.clicked.connect(self.remove_from_memory)
        self.pushButton_left_bracket.clicked.connect(lambda: self.print('(', '('))
        self.pushButton_right_bracket.clicked.connect(lambda: self.print(')', ')'))
        self.output1.setText(''.join(self.displayed_content))
        self.pushButton_help.clicked.connect(self.show_dialog)

    def change(self, command):
        self.content.append(command)

    def print(self, term, displayed_term):
        print(self.memory)
        if self.validate(term, displayed_term):
            self.content.append(term)
            self.displayed_content.append(displayed_term)
            self.output1.setText(''.join(self.displayed_content))
            temp = ''.join(self.content)
            try:
                self.result = eval(temp)
                self.output2.setText(str(self.result))
            except SyntaxError:
                pass

    def add_to_memory(self):
        self.memory = str(self.result)
        print(self.memory)

    def remove_from_memory(self):
        self.memory="0"

    def delete(self):
        if len(self.content) != 0:
            self.content.pop()
            self.displayed_content.pop()
            self.output1.setText(''.join(self.displayed_content))
            temp = ''.join(self.content)
            try:
                temp = eval(temp)
                self.output2.setText(str(temp))
            except SyntaxError:
                pass
            if len(self.content) == 0:
                self.output2.setText('0')
                self.output1.setText('0')
                self.content = ['0']
                self.displayed_content = ['0']

    def validate(self, term, displayed_term):
        if self.content == ['0'] and (term in self.numbers or (displayed_term == "M" and self.memory != "0")):
            self.content.pop()
            self.displayed_content.pop()
            return True
        elif self.content == ['0'] and term == '0':
            return False
        elif term == "0" and self.content[-1] == "/":
            self.output2.setText("Cannot divide by zero.")
            return False
        elif term in self.operators and (self.content[-1] in self.operators or self.displayed_content[-1] == "M"):
            return False
        elif term == '.' and '.' in self.content:
            return False
        elif (term == '(') and self.content[-1] not in self.operators:
            return False
        elif (term == ')') and self.content[-1] in self.operators:
            return False
        elif (self.displayed_content[-1] not in self.operators) and displayed_term == "M":
            return False
        else:
            return True
