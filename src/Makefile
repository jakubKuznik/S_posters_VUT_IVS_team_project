PYTHON = python3

PACK_NAME = xvanom00_xkuzni04_xkrato61_xsvobo1x
#ALL_DIRS = ./doc ./install ./repo	# directories in a pack

.PHONY = help test run clean doc bundle

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

pip:
	pip3 freeze

run:
	${PYTHON} calc.py

installer: calc.py math_lib.py gui.py requirements.txt
	bash install_script.sh

clean:
	rm -r *.project
