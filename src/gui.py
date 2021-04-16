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
        self.setFixedSize(290, 480)
        # TODO: icon

        # UI ELEMENTS

        self.pushButton_smem = QPushButton(self)
        self.pushButton_s_equal = QPushButton(self)
        self.pushButton_back = QtWidgets.QPushButton(self)
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
                              ["9", [150, 190, 61, 61]],
                              ["+", [220, 330, 61, 61]],
                              ["-", [220, 260, 61, 61]],
                              ["*", [220, 190, 61, 61]],
                              ["(", [10, 140, 61, 41]],
                              [")", [80, 140, 61, 41]],
                              [".", [150, 400, 61, 61]],
                              ["/", [220, 140, 61, 41]],
                              ]

        self.setup_ui()

    def setup_ui(self):
        self.resize(300, 500)
        self.setWindowTitle("Imposter Calculator")

        for i in range(len(self.digit_buttons)):
            x_coord = self.digit_buttons[i][1][0]
            y_coord = self.digit_buttons[i][1][1]
            x_size = self.digit_buttons[i][1][2]
            y_size = self.digit_buttons[i][1][3]
            text = self.digit_buttons[i][0]
            self.list_of_buttons.append(QPushButton(text, self))
            self.list_of_buttons[i].setGeometry(QtCore.QRect(x_coord, y_coord, x_size, y_size))
            self.list_of_buttons[i].clicked.connect(lambda checked, arg=text: self.print(arg, arg))

        self.pushButton_smem.setGeometry(QtCore.QRect(10, 400, 61, 61))
        self.pushButton_smem.setText("M")

        self.pushButton_s_equal.setGeometry(QtCore.QRect(220, 400, 61, 61))
        self.pushButton_s_equal.setText("=")

        self.pushButton_back.setGeometry(QtCore.QRect(150, 140, 61, 41))
        self.pushButton_back.setText("←")

        self.pushButton_smemminus.setGeometry(QtCore.QRect(220, 90, 61, 41))
        self.pushButton_smemminus.setText("M-")

        self.pushButton_sqrt.setGeometry(QtCore.QRect(80, 90, 61, 41))
        self.pushButton_sqrt.setText("[2]√")

        self.pushButton_ssqr.setGeometry(QtCore.QRect(10, 90, 61, 41))
        self.pushButton_ssqr.setText("^")

        self.pushButton_smemplus.setGeometry(QtCore.QRect(150, 90, 61, 41))
        self.pushButton_smemplus.setText("M+")


        # HELP BUTTON
        self.pushButton_help.setGeometry(QtCore.QRect(0, 0, 35, 35))
        self.pushButton_help.setText("?")
        self.pushButton_help.clicked.connect(self.help_click)

        self.output1.setGeometry(QtCore.QRect(20, 10, 251, 40))
        self.output1.setFont(QFont('Comic Sans MS', 15))
        self.output1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.output2.setGeometry(QtCore.QRect(20, 41, 251, 71))
        self.output2.setFont(QFont('Comic Sans MS', 20))

        self.pushButton_back.clicked.connect(self.delete)
        self.pushButton_ssqr.clicked.connect(lambda: self.print("**", "^"))
        self.pushButton_sqrt.clicked.connect(lambda: self.print("**0.5", "[2]√"))
        self.pushButton_smem.clicked.connect(lambda: self.print(self.memory, "M"))
        self.pushButton_smemplus.clicked.connect(self.add_to_memory)
        self.pushButton_smemminus.clicked.connect(self.remove_from_memory)
        self.output1.setText(''.join(self.displayed_content))

    ##
    # Function that opens help_form
    def help_click(self):
        self.window = QtWidgets.QApplication(sys.argv)
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

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
        self.memory = "0"

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


##
# HELP_FORM open after ? button click
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Nápověda")
        Form.resize(499, 653)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 501, 651))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Nápověda:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Zadávání:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Čísla a operace můžete zadat pomocí klávesnice, nebo myši.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Smaž poslední znak &lt;-</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.Klikni na symbol šipky zpět</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Clear C</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.Klikni na sybol C a vymaže se celá pamět</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Základní operace (+ - * /)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Pro výpočet prvně zadejte číslo</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Zvolte operaci</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. Zvolte druhé čísla</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. Zmáčkněte symbol =</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Faktoriál !</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Zvolte <span style=\" font-weight:600;\">CELÉ KLADNÉ (1, 2, 3 ...) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Stiskněte symbol faktoriálu !</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Odmocnina √</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Zvolte <span style=\" font-weight:600;\">CELÉ ČÍSLO </span>jako základ odmocniny</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Stiskněte symbol odmocniny  √</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. Zvolte číslo, které chcete odmocnit (mějte na paměti že kladná odmocnina ze záporného čísla není možná.)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Mocnina ^</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Zvolte číslo jako základ.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Zvolte číslo jako exponent</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Práce s paměti M  M+ M-</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. K uložení čísla do paměti stiskněte tlačítko <span style=\" font-weight:600;\">M+</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. K využítí čísla z paměti ve výpočtu stiskněte tlačítko<span style=\" font-weight:600;\"> M</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. Ke smazaní čísla z paměti použijte symbol <span style=\" font-weight:600;\">M-</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Práce se závorkami </span>()</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Cokoliv uvedeme do závorek bude provedeno přednostně.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Desetinná čárka ,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Pro čísla s desetinnou čárkou je zde tlačítko ,</p></body></html>"))

