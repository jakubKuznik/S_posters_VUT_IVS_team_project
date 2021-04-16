import sys

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
        self.setFixedSize(360, 480)
        # TODO: icon

        self.window = QtWidgets.QApplication(sys.argv)
        self.form = Form()

        # UI ELEMENTS
        self.pushButton_smem = QPushButton(self)
        self.pushButton_s_equal = QPushButton(self)
        self.pushButton_back = QPushButton(self)
        self.pushButton_smemminus = QPushButton(self)
        self.pushButton_sqrt = QPushButton(self)
        self.pushButton_ssqr = QPushButton(self)
        self.pushButton_smemplus = QPushButton(self)
        self.pushButton_help = QPushButton(self)
        self.pushButton_sce = QPushButton(self)
        self.output1 = QtWidgets.QLabel(self)
        self.output2 = QtWidgets.QLabel(self)
        self.list_of_buttons = []
        self.buttons = [["0", [80, 400, 61, 61]],
                        ["1", [10, 330, 61, 61]],
                        ["2", [80, 330, 61, 61]],
                        ["3", [150, 330, 61, 61]],
                        ["4", [10, 260, 61, 61]],
                        ["5", [80, 260, 61, 61]],
                        ["6", [150, 260, 61, 61]],
                        ["7", [10, 190, 61, 61]],
                        ["8", [80, 190, 61, 61]],
                        ["9", [150, 190, 61, 61]],
                        ["+", [220, 330, 61, 61]],
                        ["-", [220, 260, 61, 61]],
                        ["*", [220, 190, 61, 61]],
                        ["(", [10, 140, 61, 41]],
                        [")", [80, 140, 61, 41]],
                        [".", [150, 400, 61, 61]],
                        ["/", [220, 140, 61, 41]],
                        ["x", [290, 140, 61, 41]],
                        ["n!", [290, 190, 61, 61]],
                        ["mod", [290, 260, 61, 61]],
                        ["%", [290, 330, 61, 61]],
                        ]
        self.setup_ui()

    ## This function creates the user interface of the app, connects signals to slots.
    # @brief In a for loop, all generic buttons are created, triggers setup. Other buttons are created manually.
    #
    # @param self(App)
    #
    def setup_ui(self):
        self.setWindowTitle("Imposter Calculator")

        for i in range(len(self.buttons)):
            x_coord = self.buttons[i][1][0]
            y_coord = self.buttons[i][1][1]
            x_size = self.buttons[i][1][2]
            y_size = self.buttons[i][1][3]
            text = self.buttons[i][0]
            self.list_of_buttons.append(QPushButton(text, self))
            self.list_of_buttons[i].setGeometry(QtCore.QRect(x_coord, y_coord, x_size, y_size))
            self.list_of_buttons[i].clicked.connect(lambda checked, arg=text: self.print(arg, arg))

        self.pushButton_sce.setGeometry(QtCore.QRect(10, 400, 61, 61))
        self.pushButton_sce.setText("CE")

        self.pushButton_s_equal.setGeometry(QtCore.QRect(220, 400, 131, 61))
        self.pushButton_s_equal.setText("=")

        self.pushButton_back.setGeometry(QtCore.QRect(150, 140, 61, 41))
        self.pushButton_back.setText("←")

        self.pushButton_sqrt.setGeometry(QtCore.QRect(80, 90, 61, 41))
        self.pushButton_sqrt.setText("√")

        self.pushButton_ssqr.setGeometry(QtCore.QRect(10, 90, 61, 41))
        self.pushButton_ssqr.setText("^")

        self.pushButton_smem.setGeometry(QtCore.QRect(150, 90, 61, 41))
        self.pushButton_smem.setText("M")

        self.pushButton_smemplus.setGeometry(QtCore.QRect(220, 90, 61, 41))
        self.pushButton_smemplus.setText("M+")

        self.pushButton_smemminus.setGeometry(QtCore.QRect(290, 90, 61, 41))
        self.pushButton_smemminus.setText("M-")

        self.pushButton_help.setGeometry(QtCore.QRect(0, 0, 35, 35))
        self.pushButton_help.setText("?")
        self.pushButton_help.clicked.connect(self.help_click)

        self.output1.setGeometry(QtCore.QRect(35, 10, 320, 40))
        self.output1.setFont(QFont('Comic Sans MS', 15))
        self.output1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.output2.setGeometry(QtCore.QRect(20, 40, 320, 50))
        self.output2.setFont(QFont('Comic Sans MS', 20))

        self.pushButton_back.clicked.connect(self.delete)
        self.pushButton_ssqr.clicked.connect(lambda: self.print("**", "^"))
        self.pushButton_sqrt.clicked.connect(lambda: self.print("**0.5", "[2]√"))
        self.pushButton_smem.clicked.connect(lambda: self.print(self.memory, "M"))
        self.pushButton_smemplus.clicked.connect(self.add_to_memory)
        self.pushButton_smemminus.clicked.connect(self.remove_from_memory)
        self.output1.setText(''.join(self.displayed_content))

    ## This function reimplements the default keyPressEvent function from PyQt5
    # @brief Rebinds numbers and operators keys as new signals
    #
    # @param self(App)
    #
    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == QtCore.Qt.Key_0:
            self.print('0', '0')
        elif event.key() == QtCore.Qt.Key_1:
            self.print('1', '1')
        elif event.key() == QtCore.Qt.Key_2:
            self.print('2', '2')
        elif event.key() == QtCore.Qt.Key_3:
            self.print('3', '3')
        elif event.key() == QtCore.Qt.Key_4:
            self.print('4', '4')
        elif event.key() == QtCore.Qt.Key_5:
            self.print('5', '5')
        elif event.key() == QtCore.Qt.Key_6:
            self.print('6', '6')
        elif event.key() == QtCore.Qt.Key_7:
            self.print('7', '7')
        elif event.key() == QtCore.Qt.Key_8:
            self.print('8', '8')
        elif event.key() == QtCore.Qt.Key_9:
            self.print('9', '9')

        elif event.key() == QtCore.Qt.Key_F1:
            self.help_click()
        elif event.key() == QtCore.Qt.Key_Plus:
            self.print('+', '+')
        elif event.key() == QtCore.Qt.Key_Minus:
            self.print('-', '-')
        elif event.key() == QtCore.Qt.Key_Slash:
            self.print('/', '/')
        elif event.key() == QtCore.Qt.Key_ParenLeft:
            self.print('(', '(')
        elif event.key() == QtCore.Qt.Key_ParenRight:
            self.print(')', ')')
        elif event.key() == QtCore.Qt.Key_AsciiCircum:
            self.print("**", "^")
        elif event.key() == QtCore.Qt.Key_Period:
            self.print(".", ".")
        elif event.key() == QtCore.Qt.Key_Comma:
            self.print(".", ".")
        elif event.key() == QtCore.Qt.Key_Multi_key:
            self.print("*", "*")

    ## Slot to display the help message for user.
    # @brief Displays a short form containing instructions for basic use.
    #
    # @param sel (App)
    #
    def help_click(self):
        self.form.show()

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

    ##
    # @brief Funkce dělá ...
    #
    # @param p1 popis
    # @param p2 popis
    # @return popis výsledku
    #
    def add_to_memory(self):
        self.memory = str(self.result)
        print(self.memory)

    ##
    # @brief Funkce dělá ...
    #
    # @param p1 popis
    # @param p2 popis
    # @return popis výsledku
    #
    def remove_from_memory(self):
        self.memory = "0"

    ##
    # @brief Funkce dělá ...
    #
    # @param p1 popis
    # @param p2 popis
    # @return popis výsledku
    #
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

    ##
    # @brief Funkce dělá ...
    #
    # @param p1 popis
    # @param p2 popis
    # @return popis výsledku
    #
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


##
# HELP_FORM class to open after ? button click
class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nápověda")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 501, 651))
        self.textEdit.setReadOnly(True)
        self.textEdit.setFont(QFont('Comic Sans MS', 15))
        with open("help_form_html.txt") as f:
            self.textEdit.setHtml(''.join(f.readlines()))