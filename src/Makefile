PYTHON = python3

# .PHONY defines parts of the makefile that are not dependant on any specific file
.PHONY = help test run clean #setup

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "------------------------------------"

# This function uses unittest to test our source files
test:
	${PYTHON} -m unittest test_calc_tdd.py

run:
	${PYTHON} calc.py

clean:
	rm -r *.project
