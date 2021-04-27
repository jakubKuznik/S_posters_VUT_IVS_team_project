PYTHON = python3
DESTDIR = ../installer/DEBIAN
SHELL = /bin/bash
INSFLAGS = -m 0755

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

all: pip run
#profile:

# TO-DO create a repo structure in a pack (replace (ALLDIRS))
#pack:
#	tar cvzf $(PACK_NAME).tar.gz $(ALLDIRS)
#	zip $(PACK_NAME).zip $(ALLDIRS)

# This function creates documentation using the Doxyfile configuration
doc: Doxyfile
	cd .. && rm -rf doc
	cd .. && mkdir doc && cd doc && doxygen ../src/$^

# This function uses unittest to test our source files
test:
	${PYTHON} -m unittest test_calc_tdd.py

pip:
	pip3 freeze

init: requirements.txt
	pip3 install -r requirements.txt

run: calc.py
	${PYTHON} calc.py

dist/slothcalc/slothcalc: calc.py help_form.html bulb_on.png bulb_off.png question_off.png question_on.png icon.png
	pyi-makespec calc.py --onefile --add-data help_form.html:help_form.html --add-data bulb_on.png:bulb_on.png --add-data bulb_off.png:bulb_off.png --add-data question_on.png:question_on.png --add-data question_off.png:question_off.png --add-data icon.png:icon.png --hidden-import sip
	pyinstaller calc.spec

install: dist/slothcalc/slothcalc
	cp ./dist/calc ../installer/usr/bin/slothcalc
	cd .. && dpkg-deb --build installer

profile:
	${PYTHON} profiling.py

clean:
	rm -f ../installer/usr/bin/*
	rm -rf build
	rm -rf dist
	rm -rf ./*.spec
	cd .. && rm -rf doc
