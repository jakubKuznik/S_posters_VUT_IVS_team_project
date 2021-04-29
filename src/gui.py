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
#  @brief Calculator user interface
#
#  @author Vaňo Michal
#  @author Kuzník Jakub
#  @author Kratochvíl Pavel
#  @author Svobodová Lucie

import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtWidgets import QWidget, QPushButton, QGraphicsDropShadowEffect, QApplication
from calc_parser import *


##
# @brief This function assigns the correct path in order for pyinstaller to work.
#
# @param path
#
def get_path(path):
    if hasattr(sys, 'frozen'):
        return os.path.join(getattr(sys, '_MEIPASS'), path)
    else:
        return path

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
        self.root_base_displayed = []
        ##
        self.root_content = []
        ##
        self.root_content_displayed = []
        ##
        self.color_mode = False

        ## Global font family and size declaration.
        self.font = QFont("Arial", 16)

        ## Init of help form with font passed as a parameter.
        self.form = Form(self.font)
        self.setWindowIcon(QIcon(get_path("icon.png")))

        ## = button init.
        self.pushButton_s_equal = QPushButton(self)
        ## M button init.
        self.pushButton_mem = QPushButton(self)
        ## Primary display init.
        self.output1 = QtWidgets.QLabel(self)
        ## Secondary display init.
        self.output2 = QtWidgets.QLabel(self)
        ## Help button init.
        self.pushButton_help = QPushButton(self)
        ## Dark mode button init.
        self.pushButton_color = QPushButton(self)

        ## Color modes icons
        self.color_light = QIcon(get_path('bulb_on.png'))
        self.color_dark = QIcon(get_path('bulb_off.png'))
        self.question_on = QIcon(get_path('question_on.png'))
        self.question_off = QIcon(get_path('question_off.png'))


        ## List of all buttons in the user interface.
        self.list_of_buttons = []

        ## List of button params(coords, size, text and function).
        self.buttons = [["0", [125, 775], "M", self.print, "0", "0"],  #
                        ["1", [15, 665], "M", self.print, "1", "1"],
                        ["2", [125, 665], "M", self.print, "2", "2"],
                        ["3", [235, 665], "M", self.print, "3", "3"],
                        ["4", [15, 555], "M", self.print, "4", "4"],
                        ["5", [125, 555], "M", self.print, "5", "5"],
                        ["6", [235, 555], "M", self.print, "6", "6"],
                        ["7", [15, 445], "M", self.print, "7", "7"],
                        ["8", [125, 445], "M", self.print, "8", "8"],
                        ["9", [235, 445], "M", self.print, "9", "9"],
                        [".", [235, 775], "M", self.print, ".", "."],
                        ["CE", [15, 775], "M", self.complete_delete],
                        ["+", [345, 665], "M", self.print, "+", "+"],
                        ["-", [345, 555], "M", self.print, "-", "-"],
                        ["✕", [345, 445], "M", self.print, "*", "*"],
                        ["(", [15, 335], "S", self.print, "(", "("],
                        [")", [125, 335], "S", self.print, ")", ")"],
                        ["/", [345, 335], "S", self.print, "/", "/"],
                        ["→", [455, 335], "S", self.move_in_root],
                        ["!", [455, 445], "M", self.print, "!", "!"],
                        ["mod", [455, 555], "M", self.print, "?", "mod"],
                        ["π", [455, 665], "M", self.print, "3.1415926535", "π"],
                        ["←", [235, 335], "S", self.delete],

                        ["√", [125, 225], "S", self.root],
                        ["^", [15, 225], "S", self.print, "&", "^"],  #
                        ["M+", [345, 225], "S", self.add_to_memory],
                        ["M-", [455, 225], "S", self.remove_from_memory],
                        ]

        self.setup_ui()
        self.toggle_light_mode()

    ## User interface set up.
    # @brief Creation and setting of all button parameters, display parameters, fonts.
    #
    # @param self
    #
    def setup_ui(self):
        self.setFixedSize(550, 870)
        self.setWindowTitle("Sloth Calculator")
        for i in range(len(self.buttons)):
            x_coord = self.buttons[i][1][0]
            y_coord = self.buttons[i][1][1]

            # text displayed on the button
            text = self.buttons[i][0]

            # function to bind to key press
            callback_fn = self.buttons[i][3]

            self.list_of_buttons.append(QPushButton(text, self))
            self.list_of_buttons[i].setGeometry(QtCore.QRect(x_coord, y_coord, 80, 80))

            # if for buttons with less arguments, e.g. "←", "M", "M+", "M-",
            if len(self.buttons[i]) == 4:
                self.list_of_buttons[i].clicked.connect(lambda checked, fn=callback_fn: fn())
            else:
                term = self.buttons[i][4]
                displayed_term = self.buttons[i][5]
                self.list_of_buttons[i].clicked.connect(
                    lambda checked, t=term, d_t=displayed_term, fn=callback_fn: fn(t, d_t))

        self.pushButton_s_equal.setGeometry(QtCore.QRect(345, 775, 190, 80))
        self.pushButton_s_equal.setText("=")
        self.pushButton_s_equal.clicked.connect(lambda: self.evaluate())
        self.list_of_buttons.append(self.pushButton_s_equal)

        self.pushButton_mem.setGeometry(QtCore.QRect(235, 225, 80, 80))
        self.pushButton_mem.setText("M")
        self.pushButton_mem.clicked.connect(lambda: self.print(self.memory, "M"))
        self.list_of_buttons.append(self.pushButton_mem)

        self.output1.setGeometry(QtCore.QRect(0, 0, 550, 105))
        self.output1.setFont(self.font)
        self.output1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.output1.setText(''.join(self.displayed_content))
        self.output1.setFont(QFont("Arial", 20))

        self.output2.setGeometry(QtCore.QRect(0, 105, 550, 105))
        self.output2.setFont(QFont("Arial", 35))

        self.pushButton_help.setGeometry(QtCore.QRect(16, 60, 30, 30))
        self.pushButton_help.clicked.connect(self.help_click)
        self.pushButton_help.setIconSize(QSize(30, 30))
        self.list_of_buttons.append(self.pushButton_help)

        self.pushButton_color.setGeometry(14, 15, 35, 35)
        self.pushButton_color.setCheckable(True)
        self.pushButton_color.clicked.connect(self.change_color)
        self.list_of_buttons.append(self.pushButton_color)

        # setting default font to each button
        for i in range(len(self.list_of_buttons)):
            self.list_of_buttons[i].setFont(self.font)

    ## Dark/light mode helper switch function.
    # @brief According to the toggle button state changes color mode of calculator.
    #
    # @param self
    def change_color(self):
        if self.color_mode:
            self.toggle_light_mode()
            self.color_mode = False
        else:
            self.toggle_dark_mode()
            self.color_mode = True


    ## Function which changes components' color to dark mode.
    # @brief Changes color of all buttons and background.
    #
    # @param self
    #
    def toggle_dark_mode(self):
        self.pushButton_color.setIcon(self.color_dark)
        self.pushButton_help.setIcon(self.question_off)

        # background
        self.setStyleSheet("background-color: rgb(68, 68, 68);")

        # numpad
        for j in range(12):
            self.list_of_buttons[j].setStyleSheet("QPushButton {background-color: rgb(68, 68, 68); color: rgb(206, 206, 206); border-radius: 50; border-color: rgb(214, 237, 255)} QPushButton:pressed{background-color: rgb(248, 226, 228); border: 3px solid; border-color:green;}")

        # round buttons
        for j in range(12, len(self.list_of_buttons) - 6):
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(40)
            shadow.setOffset(-3, 10)
            shadow.setColor(QColor(58, 58, 58))

            self.list_of_buttons[j].setStyleSheet("QPushButton {color: rgb(255, 100, 100); border-radius: 40; background-color: rgb(96, 96, 96);} QPushButton:pressed{border: 3px solid; border-color:green;}")
            self.list_of_buttons[j].setGraphicsEffect(shadow)

        # upper
        for j in range(len(self.list_of_buttons) - 6, len(self.list_of_buttons)):
            self.list_of_buttons[j].setStyleSheet("QPushButton {color: rgb(206, 206, 206); background-color: rgb(68, 68, 68);border: 0px;} QPushButton:pressed{border: 3px solid; border-color:green;}")

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setOffset(-3, 5)
        shadow.setColor(QColor(58, 58, 58))
        self.pushButton_s_equal.setStyleSheet("QPushButton{background-color: rgb(255, 100, 100); border-radius: 30%;color: white;} QPushButton:pressed {border: 5px solid; border-color:rgb(117, 117, 117); color: white;}")
        self.pushButton_s_equal.setGraphicsEffect(shadow)
        self.pushButton_help.setStyleSheet("background-color: rgb(48, 48, 48);border: 0px;")
        self.pushButton_color.setStyleSheet("background-color: rgb(48, 48, 48);border: 0px;")
        self.output1.setStyleSheet("color: rgb(148, 148, 148); background-color: rgb(48, 48, 48); padding-left:35px;padding-right:15px;")
        self.output2.setStyleSheet("color: rgb(255, 100, 100); background-color: rgb(48, 48, 48); padding-left:20px;")

    ## Function which changes components' color to light(default) mode.
    # @brief Changes color of all buttons and background.
    #
    # @param self
    #
    def toggle_light_mode(self):
        self.pushButton_color.setIcon(self.color_light)
        self.pushButton_color.setIconSize(QSize(35, 35))
        self.pushButton_help.setIcon(self.question_on)

        # background
        self.setStyleSheet("background-color: rgb(248, 248, 248);")

        # numpad
        for j in range(12):
            self.list_of_buttons[j].setStyleSheet("QPushButton{background-color: rgb(248, 248, 248); color: rgb(117, 117, 117); border-radius: 50; border-color: rgb(214, 237, 255)} QPushButton:pressed{border-radius:40; background-color: rgb(206, 206, 206);color: rgb(96, 96, 96)}")

        # all other buttons
        for j in range(12, len(self.list_of_buttons)-6):
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(30)
            shadow.setOffset(-3, 5)
            shadow.setColor(QColor(224, 200, 203))

            self.list_of_buttons[j].setStyleSheet("QPushButton{color: rgb(255, 100, 100); border-radius: 40; background-color: rgb(248, 226, 228);} QPushButton:pressed{border: 3px solid; border-color:green;}")
            self.list_of_buttons[j].setGraphicsEffect(shadow)

        for j in range(len(self.list_of_buttons) - 6, len(self.list_of_buttons)):
            self.list_of_buttons[j].setStyleSheet("QPushButton{color: rgb(117, 117, 117); background-color: rgb(248, 248, 248);border: 0px;} QPushButton:pressed{border: 3px solid; border-color:rgb(117, 117, 117);}")

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setOffset(-3, 5)
        shadow.setColor(QColor(236, 159, 166))
        self.pushButton_s_equal.setStyleSheet("QPushButton{background-color: rgb(255, 100, 100); border-radius: 30%;color:white;} QPushButton:pressed { border: 5px solid; border-color:rgb(117, 117, 117);color:white;}")
        self.pushButton_s_equal.setGraphicsEffect(shadow)
        self.pushButton_help.setStyleSheet("background-color:white; border: 0px;")
        self.pushButton_color.setStyleSheet("background-color:white; border: 0px;")
        self.output1.setStyleSheet("color: rgb(170, 170, 170); background-color: white; padding-left:35px;padding-right:15px;")
        self.output2.setStyleSheet("color: rgb(255, 100, 100); background-color: white; padding-left:20px;")

    ## This function maps keyboard keys to buttons in the user interface
    # @brief Rebinds PyQt's default numbers and operators keys as new signals
    #
    # @param self
    # @param event An argument that is passed on pressing a button.
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
        elif event.key() == QtCore.Qt.Key_ParenLeft:
            self.print("(", "(")
        elif event.key() == QtCore.Qt.Key_ParenRight:
            self.print(")", ")")
        elif event.key() == QtCore.Qt.Key_P:
            self.print("3.1415926535", "π")
        elif event.key() == QtCore.Qt.Key_M:
            self.print(self.memory, "M")
        elif event.key() == QtCore.Qt.Key_Delete:
            self.complete_delete()
        elif event.key() == QtCore.Qt.Key_Return:
            self.evaluate("Pressed")
        elif event.key() == QtCore.Qt.Key_R:
            self.root()
        elif event.key() == QtCore.Qt.Key_Exclam:
            self.print("!", "!")
        elif event.key() == QtCore.Qt.Key_Percent:
            self.print("?","mod")
        elif event.key() == QtCore.Qt.Key_B:
            self.add_to_memory()
        elif event.key() == QtCore.Qt.Key_N:
            self.remove_from_memory()
        elif event.key() == QtCore.Qt.Key_C:
            self.complete_delete()
        elif event.key() == QtCore.Qt.Key_D:
            self.change_color()
        else:
            pass
    ## This function evaluates user input.
    # @brief Sends string input to parser for further evaluation.
    #
    # @param self
    # @param root Optional parameter that tells the evaluate function who called it and in which context, as evaluate has two functions: Move inside of the root, Evaluate the entire expression.
    def evaluate(self, root=None):
        if self.inRoot==True and root=="Pressed":
            self.move_in_root()
        else:
            if root != "Content" and root != "Base":
                if self.content != [] and not self.inRoot:
                    self.result = split_string_fn(self.content, self.displayed_content)
                    print(self.result)
                    if self.result!="Syntax Error" and self.result!="Math Error":
                        if len(str(self.result))>16:
                            self.output2.setText('{:.14g}'.format(float(self.result)))
                        else:
                            if float(self.result).is_integer():
                                self.output2.setText(str(int(float(self.result))))

                            else:
                                self.output2.setText(str(self.result))
                    else:
                        self.output2.setText(self.result)
            else:
                if root == "Content":
                    return split_string_fn(self.root_content, self.root_content_displayed)
                else:
                    return split_string_fn(self.root_base, self.root_base_displayed)
    ##
    # @brief Prepares the environment for root typesetting
    #
    # @param self
    #
    def root(self):
        if not self.inRoot:
            self.displayed_content.append('[~~]')
            self.displayed_content.append('√')
            self.displayed_content.append('(~~)')
            self.output1.setText(''.join(self.displayed_content))
            self.inRoot = True

    # @brief Moves inside of the root and evaluates the expressions inside of root brackets.
    #
    # @param self
    #
    def move_in_root(self):
        if self.inRoot:
            if self.rootCounter == 0:
                self.rootCounter = 1
            elif self.rootCounter == 1:
                root_content_result = str(self.evaluate("Content"))
                self.content.append('(')
                self.content.append(root_content_result)
                self.content.append(')')
                self.content.append("$")
                self.content.append('(')
                root_base_result = str(self.evaluate("Base"))
                self.content.append(root_base_result)
                self.content.append(')')
                self.root_content = []
                self.root_base = []
                self.root_content_displayed = []
                self.root_base_displayed = []
                self.rootCounter = 0
                self.inRoot = False

    # @brief Types inside of the root brackets.
    #
    # @param term Allows different behavior based on whether the user pressed a binary or a unary operation.
    # @param displayed_term Allows different behavior based on whether the user pressed a binary or a unary operation.
    def type_in_root(self, term, displayed_term):
        if self.rootCounter == 0:
            if term != '!':
                self.root_base.append(term)
            else:
                self.root_base.append(term)
                self.root_base.append('0')

            self.root_base_displayed.append(displayed_term)

            self.displayed_content[-3] = '[' + ''.join(self.root_base_displayed) + ']'
            self.output1.setText(''.join(self.displayed_content))

        if self.rootCounter == 1:
            if term != '!':
                self.root_content.append(term)
            else:
                self.root_content.append(term)
                self.root_content.append('0')

            self.root_content_displayed.append(displayed_term)
            self.displayed_content[-1] = '(' + ''.join(self.root_content_displayed) + ')'
            self.output1.setText(''.join(self.displayed_content))

    # @brief Shows the help window.
    #
    # @param self
    #
    def help_click(self):
        self.form.show()

    # @brief Prints the pressed or clicked token if it is possible.
    #
    # @param term Allows different behavior based on whether the user pressed a binary or a unary operation.
    # @param displayed_term Allows different behavior based on whether the user pressed a binary or a unary operation.
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
        else:
            self.type_in_root(term, displayed_term)

    ##
    # @brief Overwrites the current memory by the current result.
    #
    # @param self
    def add_to_memory(self):
        if 'e' in str(self.result):
            pass
        else:
            self.memory=str(self.result)

    ##
    # @brief Deletes the current memory, setting it to zero.
    #
    # @param self
    def remove_from_memory(self):
        self.memory = "0"

    ##
    # @brief Deletes the last item in the displayed content with special rules regarding root.
    #
    # @param self
    def delete(self):
        if len(self.content) != 0 or self.inRoot:
            if self.displayed_content[-1] == '!':
                self.content.pop()
                self.content.pop()
                self.displayed_content.pop()
            elif self.inRoot:
                self.root_content = []
                self.root_base = []
                self.root_content_displayed = []
                self.root_base_displayed = []
                self.displayed_content.pop()
                self.displayed_content.pop()
                self.displayed_content.pop()
                self.inRoot = False
                self.rootCounter = 0
            elif len(self.displayed_content[-1]) > 1 and self.displayed_content[-1][-1] == ')':
                self.displayed_content.pop()
                self.displayed_content.pop()
                self.displayed_content.pop()
                for i in range(7):
                    self.content.pop()
            else:
                self.content.pop()
                self.displayed_content.pop()
            self.output1.setText(''.join(self.displayed_content))

    ## This function deletes the entire content of the display.
    #
    # @param self
    #
    def complete_delete(self):
        self.content = []
        self.displayed_content = []
        self.output1.setText(''.join(self.displayed_content))
        self.output2.setText(''.join(self.content))
        self.root_content = []
        self.root_base = []
        self.root_content_displayed = []
        self.root_base_displayed = []
        self.inRoot=False


## Help form window class
# @brief Displays help document to the user describing basic usage of all operators.
#        Inherits from the QWidget class.
# @param font is later set as the default font
class Form(QWidget):
    ## Init function of the Form class.
    # @brief Initializes HTML canvas, sets default font(passed as param from the App class instance), displays content
    # help_form.html
    #
    # @param self
    # @param font Sets the font of the text
    def __init__(self, font):
        super().__init__()
        self.setWindowTitle("Nápověda")
        ## Text edit HTML canvas for displaying help
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 501, 651))
        self.textEdit.setReadOnly(True)
        self.textEdit.setFont(font)
        with open(get_path('help_form.html'), encoding='utf-8') as f:
            self.textEdit.setHtml(''.join(f.readlines()))
