#!/usr/bin/env python
# ##########################################
# Project name: IVS - projekt
# File: profiling.py
# Date: 24. 04. 2021
# Last change: 28. 04. 2021
# Team: S_POSTERS
# Supervisor: ...
# Authors:  Vaňo Michal
#           Kuzník Jakub
#           Kratochvíl Pavel
#           Svobodová Lucie
# ##########################################

## A script used for profiling. Runs the program standard_deviation.py.
#
#  @package profiling
#  @file profiling.py
#
#  @brief A script used for profiling. Runs the program standard_deviation.py.
#
#  @author Vaňo Michal
#  @author Kuzník Jakub
#  @author Kratochvíl Pavel
#  @author Svobodová Lucie

import standard_deviation   # program that is profiled
import cProfile             # profiler

def main():
    standard_deviation.main()

if __name__ == '__main__':
    import cProfile
    cProfile.run('main()', "../profiling/vystup.pstat")