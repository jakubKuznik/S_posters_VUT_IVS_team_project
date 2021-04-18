##########################################
# Project name: IVS - projekt
# File: gui.py
# Date: 25. 03. 2021
# Last change: 16. 04. 2021
# Team: S_POSTERS
# Supervisor: ...
# Authors:  Vaňo Michal
#           Kuzník Jakub
#           Kratochvíl Pavel
#           Svobodová Lucie
#
# Brief: GUI for our calculator
###########################################

## @file gui.py
#
#  @brief calculator gui
#
#  @author Vaňo Michal
#  @author Kuzník Jakub
#  @author Kratochvíl Pavel
#  @author Svobodová Lucie

import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QWidget, QPushButton

##
# @brief Class that
#
#
# Description
#
#
#


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

        # Load the font:
        self.font = QFont("Arial", 20)

        self.window = QtWidgets.QApplication(sys.argv)
        self.form = Form(self.font)

        # UI ELEMENTS
        self.pushButton_s_equal = QPushButton(self)
        self.pushButton_mem = QPushButton(self)
        self.pushButton_help = QPushButton(self)
        self.output1 = QtWidgets.QLabel(self)
        self.output2 = QtWidgets.QLabel(self)
        self.pushButton_color = QPushButton(self)

        self.list_of_buttons = []

        # visible text, coordinates, size (S = small button, M = medium button, L=large button),
        # callback function, term, displayed term
        self.buttons = [["0", [80, 400], "M", self.print, "0", "0"],
                        ["1", [10, 330], "M", self.print, "1", "1"],
                        ["2", [80, 330], "M", self.print, "2", "2"],
                        ["3", [150, 330], "M", self.print, "3", "3"],
                        ["4", [10, 260], "M", self.print, "5", "4"],
                        ["5", [80, 260], "M", self.print, "5", "5"],
                        ["6", [150, 260], "M", self.print, "6", "6"],
                        ["7", [10, 190], "M", self.print, "7", "7"],
                        ["8", [80, 190], "M", self.print, "8", "8"],
                        ["9", [150, 190], "M", self.print, "9", "9"],
                        ["+", [220, 330], "M", self.print, "+", "+"],
                        ["-", [220, 260], "M", self.print, "-", "-"],
                        ["*", [220, 190], "M", self.print, "*", "*"],
                        ["(", [10, 140], "S", self.print, "(", "("],
                        [")", [80, 140], "S", self.print, ")", ")"],
                        [".", [150, 400], "M", self.print, ".", "."],
                        ["/", [220, 140], "S", self.print, "/", "/"],
                        ["%", [290, 140], "S", self.print, "%", "%"],
                        ["n!", [290, 190], "M", self.print, "!", "!"],
                        ["mod", [290, 260], "M", self.print, "?", "?"],
                        ["%", [290, 330], "M", self.print, "%", "%"],
                        ["CE", [10, 400], "M", self.print, "!", "!"],
                        ["←", [150, 140], "S", self.delete],
                        ["√", [80, 90], "S", self.print, "**0.5", "[2]√"],
                        ["^", [10, 90], "S", self.print, "**", "^"],
                        ["M+", [220, 90], "S", self.add_to_memory],
                        ["M-", [290, 90], "S", self.remove_from_memory],
                        ]
        self.setup_ui()
        self.toggle_light_mode()

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

            # text displayed on the button
            text = self.buttons[i][0]

            # function to bind to key press
            callback_fn = self.buttons[i][3]

            # constant for every button except "="
            size_x = 60

            # assigning correct size according to the letter
            if self.buttons[i][2] == "S":
                size_y = 45
            elif self.buttons[i][2] == "M":
                size_y = 65
            else:
                size_y = 3

            self.list_of_buttons.append(QPushButton(text, self))
            self.list_of_buttons[i].setGeometry(QtCore.QRect(x_coord, y_coord, size_x, size_y))

            # if for buttons with less arguments, e.g. "←", "M", "M+", "M-",
            if len(self.buttons[i]) == 4:
                self.list_of_buttons[i].clicked.connect(lambda checked, fn=callback_fn: fn())
            else:
                term = self.buttons[i][4]
                print(term)
                displayed_term = self.buttons[i][5]
                self.list_of_buttons[i].clicked.connect(lambda checked, t=term, d_t=displayed_term, fn=callback_fn: fn(t, d_t))

        self.pushButton_s_equal.setGeometry(QtCore.QRect(220, 400, 130, 65))
        self.pushButton_s_equal.setText("=")
        self.list_of_buttons.append(self.pushButton_s_equal)

        self.pushButton_mem.setGeometry(QtCore.QRect(150, 90, 60, 45))
        self.pushButton_mem.setText("M")
        self.pushButton_mem.clicked.connect(lambda:  self.print(self.memory, "M"))
        self.list_of_buttons.append(self.pushButton_mem)

        self.pushButton_help.setGeometry(QtCore.QRect(0, 0, 35, 35))
        self.pushButton_help.setText("?")
        self.pushButton_help.clicked.connect(self.help_click)
        self.list_of_buttons.append(self.pushButton_help)

        self.output1.setGeometry(QtCore.QRect(35, 10, 320, 40))
        self.output1.setFont(self.font)
        self.output1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.output1.setText(''.join(self.displayed_content))

        self.output2.setGeometry(QtCore.QRect(35, 40, 320, 50))
        self.output2.setFont(self.font)

        self.pushButton_color.setGeometry(0, 35, 35, 35)
        self.pushButton_color.setCheckable(True)
        self.pushButton_color.setText("D")
        self.pushButton_color.clicked.connect(self.change_color)
        self.list_of_buttons.append(self.pushButton_color)

        # setting default font to each button
        for i in range(len(self.list_of_buttons)):
            self.list_of_buttons[i].setFont(self.font)

    def change_color(self):
        if self.pushButton_color.isChecked():
            self.toggle_dark_mode()
        else:
            self.toggle_light_mode()

    def toggle_dark_mode(self):
        # background
        self.setStyleSheet("background-color: rgb(40,54,55);")

        # numpad
        for j in range(len(self.list_of_buttons)):
            self.list_of_buttons[j].setStyleSheet("color: rgb(0, 151, 136); border-radius: 100%")

        # all other buttons
        for j in range(10, len(self.list_of_buttons)):
            self.list_of_buttons[j].setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(86, 73, 76); border-radius: 15px; border-color: rgb(214, 237, 255)")

    def toggle_light_mode(self):
        # background
        self.setStyleSheet("background-color: white;")

        # numpad
        for j in range(len(self.list_of_buttons)):
            self.list_of_buttons[j].setStyleSheet(
                "background-color: rgb(255, 255, 255); color: rgb(86, 73, 76); border-radius: 15px; border-color: rgb(214, 237, 255)")

        # all other buttons
        for j in range(10, len(self.list_of_buttons)):
            self.list_of_buttons[j].setStyleSheet("color: rgb(0, 151, 136); border-radius: 15px")

    ## This function reimplements the default keyPressEvent function from PyQt5
    # @brief Rebinds numbers and operators keys as new signals
    #
    # @param self(App)
    #
    def keyPressEvent(self, event):
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
        # TODO: zvysne tlacitka, ktore sa daju zadat z klavesnice

    ## Slot to display the help message for user.
    # @brief Displays a short form containing instructions for basic use.
    #
    # @param self(App)
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
    def __init__(self, font):
        super().__init__()
        self.setWindowTitle("Nápověda")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 501, 651))
        self.textEdit.setReadOnly(True)
        self.textEdit.setFont(font)
        with open("help_form.html", encoding='utf-8') as f:
            self.textEdit.setHtml(''.join(f.readlines()))