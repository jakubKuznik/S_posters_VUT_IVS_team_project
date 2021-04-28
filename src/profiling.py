#!/usr/bin/env python

import standard_deviation
import cProfile

def main():
    standard_deviation.main()

if __name__ == '__main__':
    import cProfile
    cProfile.run('main()', "../profiling/vystup.pstat")