#!/usr/bin/env python3
# ##########################################
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
# ##########################################

## The two scripts calc and gui form the front-end of the calculator.
# 
#  @package calc
#  @file calc.py
#
#  @brief Main script that creates an instance of the PyQt app and performs the main loop.
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
calc = QtWidgets.QApplication(sys.argv)
app = App()
app.show()
sys.exit(calc.exec_())

