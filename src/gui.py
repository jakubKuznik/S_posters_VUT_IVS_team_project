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
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton
from calc_parser import *


## Main window class
# @brief Class of the entire PyQt GUI of the calculator. Connects user interaction with backend evaluation
#
#
# Handles interaction, button presses, displays evaluated equations, shows user help form and handles light/dark mode
# changes.
#
#
class App(QWidget):
    ## Init function of the App class.
    # @brief Initializes all configuration parameters as well as global parameters for user interface.
    #
    # @param self
    #
    def __init__(self):
        super().__init__()
        ## visible content of the display
        self.content = []
        ##
        self.memory = '0'
        ##
        self.displayed_content = []
        ##
        self.result = 0
        ##
        self.operators = ['+', '-', '*', '/', '**0.5', '.', '**']
        ##
        self.numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        ##
        self.rootCounter = 0
        ##
        self.inRoot = False
        ##
        self.root_base = []
        ##
        self.root_content = []
        # TODO: icon

        ## Global font family and size declaration.
        self.font = QFont("Arial", 20)
        ## QtWidgets window init.
        self.window = QtWidgets.QApplication(sys.argv)
        ## Init of help form with font passed as a parameter.
        self.form = Form(self.font)

        ## = button init.
        self.pushButton_s_equal = QPushButton(self)
        ## M button init.
        self.pushButton_mem = QPushButton(self)
        ## Help button init.
        self.pushButton_help = QPushButton(self)
        ## Primary display init.
        self.output1 = QtWidgets.QLabel(self)
        ## Secondary display init.
        self.output2 = QtWidgets.QLabel(self)
        ## Dark mode button init.
        self.pushButton_color = QPushButton(self)

        ## List of all buttons in the user interface.
        self.list_of_buttons = []

        ## List of button params(coords, size, text and function).
        self.buttons = [["0", [80, 400], "M", self.print, "0", "0"],
                        ["1", [10, 330], "M", self.print, "1", "1"],
                        ["2", [80, 330], "M", self.print, "2", "2"],
                        ["3", [150, 330], "M", self.print, "3", "3"],
                        ["4", [10, 260], "M", self.print, "4", "4"],
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
                        ["→", [290, 140], "S", self.move_in_root],
                        ["n!", [290, 190], "M", self.print, "!", "!"],
                        ["mod", [290, 260], "M", self.print, "?", "mod"],
                        ["π", [290, 330], "M", self.print, "3.1415926535", "π"],
                        ["CE", [10, 400], "M", self.complete_delete],
                        ["←", [150, 140], "S", self.delete],
                        ["√", [80, 90], "S", self.root],
                        ["^", [10, 90], "S", self.print, "&", "^"],
                        ["M+", [220, 90], "S", self.add_to_memory],
                        ["M-", [290, 90], "S", self.remove_from_memory],
                        ]
        self.setup_ui()
        self.toggle_light_mode()

    ## User interface set up.
    # @brief Creation and setting of all button parameters, display parameters, fonts.
    #
    # @param self
    #
    def setup_ui(self):
        self.setFixedSize(360, 480)
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
                self.list_of_buttons[i].clicked.connect(
                    lambda checked, t=term, d_t=displayed_term, fn=callback_fn: fn(t, d_t))

        self.pushButton_s_equal.setGeometry(QtCore.QRect(220, 400, 130, 65))
        self.pushButton_s_equal.setText("=")
        self.pushButton_s_equal.clicked.connect(lambda: self.evaluate())
        self.list_of_buttons.append(self.pushButton_s_equal)

        self.pushButton_mem.setGeometry(QtCore.QRect(150, 90, 60, 45))
        self.pushButton_mem.setText("M")
        self.pushButton_mem.clicked.connect(lambda: self.print(self.memory, "M"))
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
        # TODO: maybe add icon for this button?
        self.pushButton_color.clicked.connect(self.change_color)
        self.list_of_buttons.append(self.pushButton_color)

        # setting default font to each button
        for i in range(len(self.list_of_buttons)):
            self.list_of_buttons[i].setFont(self.font)

    ## Dark/light mode helper switch function.
    # @brief According to the toggle button state changes color mode of calculator.
    #
    # @param self
    #
    def change_color(self):
        if self.pushButton_color.isChecked():
            self.toggle_dark_mode()
        else:
            self.toggle_light_mode()

    ## Function which changes components' color to dark mode.
    # @brief Changes color of all buttons and background.
    #
    # @param self
    #
    def toggle_dark_mode(self):
        # background
        self.setStyleSheet("background-color: rgb(40,54,55);")

        # numpad
        for j in range(len(self.list_of_buttons)):
            self.list_of_buttons[j].setStyleSheet("color: rgb(0, 151, 136); border-radius: 100%")

        # all other buttons
        for j in range(10, len(self.list_of_buttons)):
            self.list_of_buttons[j].setStyleSheet(
                "background-color: rgb(255, 255, 255); color: rgb(86, 73, 76); border-radius: 15px; border-color: rgb(214, 237, 255)")

    ## Function which changes components' color to light(default) mode.
    # @brief Changes color of all buttons and background.
    #
    # @param self
    #
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

    ## This function maps keyboard keys to buttons in the user interface
    # @brief Rebinds PyQt's default numbers and operators keys as new signals
    #
    # @param self
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
        elif event.key() == QtCore.Qt.Key_AsciiCircum:
            self.print("&", "^")
        elif event.key() == QtCore.Qt.Key_Period:
            self.print(".", ".")
        elif event.key() == QtCore.Qt.Key_Comma:
            self.print(".", ".")
        elif event.key() == QtCore.Qt.Key_Backspace:
            self.delete()
        elif event.key() == QtCore.Qt.Key_Asterisk:
            self.print("*", "*")
        elif event.key() == QtCore.Qt.Key_BracketLeft:
            self.print("(", "(")
        elif event.key() == QtCore.Qt.Key_BracketRight:
            self.print(")", ")")
        elif event.key() == QtCore.Qt.Key_Delete:
            self.complete_delete()
        elif event.key() == QtCore.Qt.Key_Return:
            self.move_in_root()
        # TODO: zvysne tlacitka, ktore sa daju zadat z klavesnice

    ## This function evaluates user input.
    # @brief Sends string input to parser for further evaluation.
    #
    # @param self
    #
    def evaluate(self):
        # self.result = SplitString(''.join(self.content))
        self.result = SplitString(self.content, self.displayed_content)
        self.output2.setText(str(self.result))

    ## This function evaluates user input.
    # @brief Sends string input to parser for further evaluation.
    #
    # @param self(App)
    #
    def root(self):
        self.displayed_content.append('[ ]')
        self.displayed_content.append('√')
        self.displayed_content.append('( )')
        self.output1.setText(''.join(self.displayed_content))
        self.inRoot = True

    ## This function evaluates user input.
    # @brief Sends string input to parser for further evaluation.
    #
    # @param self(App)
    #
    def move_in_root(self):
        if self.inRoot:
            if self.rootCounter == 0:
                self.rootCounter = 1
            elif self.rootCounter == 1:
                self.rootCounter = 0
                self.inRoot = False
                self.content.append(''.join(self.root_content))
                self.content.append("$")
                self.content.append(''.join(self.root_base))
                self.root_content = []
                self.root_base = []

    ## This function evaluates user input.
    # @brief Sends string input to parser for further evaluation.
    #
    # @param self(App)
    #
    def type_in_root(self, term):
        if self.rootCounter == 0:
            self.root_base.append(term)
            self.displayed_content[-3] = '[' + ''.join(self.root_base) + ']'
            self.output1.setText(''.join(self.displayed_content))
        if self.rootCounter == 1:
            self.root_content.append(term)
            self.displayed_content[-1] = '(' + ''.join(self.root_content) + ')'
            self.output1.setText(''.join(self.displayed_content))

    ## This function evaluates user input.
    # @brief Sends string input to parser for further evaluation.
    #
    # @param self(App)
    #
    def help_click(self):
        self.form.show()

    ## This function evaluates user input.
    # @brief Sends string input to parser for further evaluation.
    #
    # @param self(App)
    #
    def change(self, command):
        self.content.append(command)

    ## This function evaluates user input.
    # @brief Sends string input to parser for further evaluation.
    #
    # @param self(App)
    #
    def print(self, term, displayed_term):
        if not self.inRoot:
            if term != '!':
                self.content.append(term)
            else:
                self.content.append(term)
                self.content.append('0')
            self.displayed_content.append(displayed_term)
            self.output1.setText("".join(self.displayed_content))
            print(self.content)
            print(self.displayed_content)
        else:
            if term in self.numbers:
                self.type_in_root(term)
            else:
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
    # @brief Function deletes last number or operator from display
    #
    # @param self(App)
    #
    def delete(self):
        if len(self.content) != 0:
            if self.displayed_content[-1] == '!':
                self.content.pop()
                self.content.pop()
                self.displayed_content.pop()
            elif self.inRoot:
                self.root_content = []
                self.root_base = []
                self.displayed_content.pop()
                self.displayed_content.pop()
                self.displayed_content.pop()
                self.inRoot = False
                self.rootCounter = 0
            elif len(self.displayed_content[-1]) > 1 and self.displayed_content[-1][-1] == ')':
                self.displayed_content.pop()
                self.displayed_content.pop()
                self.displayed_content.pop()
                self.content.pop()
                self.content.pop()
                self.content.pop()
            else:
                self.content.pop()
                self.displayed_content.pop()
            self.output1.setText(''.join(self.displayed_content))

    ## This function deletes the entire content of the display.
    #
    # @param self(App)
    #
    def complete_delete(self):
        self.content = []
        self.displayed_content = []
        self.output1.setText(''.join(self.displayed_content))
        self.output2.setText(''.join(self.content))


## Help form window class
# @brief Displays help document to the user describing basic usage of all operators.
#        Inherits from the QWidget class.
# @param font is later set as the default font
class Form(QWidget):
    ## Init function of the Form class.
    # @brief Initializes HTML canvas, sets default font(passed as param from the App class instance), displays content
    # help_form.html
    #
    # @param self(App)
    #
    def __init__(self, font):
        super().__init__()
        self.setWindowTitle("Nápověda")
        ## Text edit HTML canvas for displaying help
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 501, 651))
        self.textEdit.setReadOnly(True)
        self.textEdit.setFont(font)
        with open("help_form.html", encoding='utf-8') as f:
            self.textEdit.setHtml(''.join(f.readlines()))
