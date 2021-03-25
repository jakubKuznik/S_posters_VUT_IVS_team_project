PYTHON = python3

PACK_NAME = xvanom00_xkuzni04_xkrato61_xsvobo1x
#ALL_DIRS = ./doc ./install ./repo	# directories in a pack

# .PHONY defines parts of the makefile that are not dependant on any specific file
.PHONY = help test run clean doc

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
# to-do later: .DEFAULT_GOAL = all
.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "To generate the documentation type make doc"
	@echo "------------------------------------"

#all:
#profile:

# TO-DO create a repo structure in a pack (replace (ALLDIRS))
#pack:
#	tar cvzf $(PACK_NAME).tar.gz $(ALLDIRS)
#	zip $(PACK_NAME).zip $(ALLDIRS)

doc:
	cd .. && mkdir doc && cd doc && doxygen ../src/Doxyfile

# This function uses unittest to test our source files
test:
	${PYTHON} -m unittest test_calc_tdd.py

run:
	${PYTHON} calc.py

clean:
	rm -r *.project
