###########################################
# Project name: IVS - projekt
# File: calc.py
# Date: 13. 03. 2021
# Last change: 13. 03. 2021
# Team: S_POSTERS
# Supervisor: ...
# Authors:  Vaňo Michal
#           Kuzník Jakub
#           Kratochvíl Pavel
#           Svobodová Lucie
#
# Brief: Calculator
###########################################

## @file calc.py
#
#  @brief calculator
#
#  @author Vaňo Michal
#  @author Kuzník Jakub
#  @author Kratochvíl Pavel
#  @author Svobodová Lucie
import sys
import time
# Mathematical library of all operation and Exceptions
import math_lib

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui import *


##
# Function ll create window that was create
# button click meaning
# n == number_button (0 1 2 3)
# s == symbol button (div, mult, percent ....)
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_s_cals()
        self.ui.setupUi(self)
        self.show()


## Documentation for a function.
#  This is how doxygen function documentation looks like .
def main():
    calc = QApplication(sys.argv)
    Main()
    sys.exit(calc.exec_())


#This is hou the main function is defined in python
if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
