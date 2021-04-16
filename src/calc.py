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
from gui import *


## This function initializes the app window.
# @brief The main function which launches the calculator app itself.
#
def main():
    calc = QtWidgets.QApplication(sys.argv)
    app = App()
    app.show()
    sys.exit(calc.exec_())


if __name__ == '__main__':
    main()
