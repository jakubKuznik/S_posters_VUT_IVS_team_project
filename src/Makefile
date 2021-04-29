PYTHON = python3
DESTDIR = ../slothcalc/DEBIAN
SHELL = /bin/bash
INSFLAGS = -m 0755

PACK_NAME = xvanom00_xkuzni04_xkrato61_xsvobo1x

.PHONY = help test run clean doc bundle

all: pip run

pip:
	pip3 freeze

init: requirements.txt
	pip3 install -r requirements.txt

run: calc.py
	${PYTHON} calc.py

# Create documentation using the Doxyfile configuration
doc: Doxyfile
	cd .. && rm -rf doc
	cd .. && mkdir doc && cd doc && doxygen ../src/$^

# Run tests
test:
	${PYTHON} -m unittest test_calc_tdd.py

# Installation
install: dist/slothcalc/slothcalc
	mkdir ../slothcalc/usr/bin
	cp ./dist/calc ../slothcalc/usr/bin/slothcalc
	cd .. && dpkg-deb --build slothcalc

dist/slothcalc/slothcalc: calc.py help_form.html bulb_on.png bulb_off.png question_off.png question_on.png icon.png
	pyi-makespec calc.py --onefile --add-data help_form.html:. --add-data bulb_on.png:. --add-data bulb_off.png:. --add-data question_on.png:. --add-data question_off.png:. --add-data icon.png:.
	pyinstaller calc.spec

# Run profiling
profile:
	${PYTHON} profiling.py

# Pack folder
pack: doc pack_folder xvanom00_xkuzni04_xkrato61_xsvobo1x.zip
xvanom00_xkuzni04_xkrato61_xsvobo1x.zip:
	cd ../.. && zip -rm $@ $(PACK_NAME)

pack_folder:
	rm -rf ../../xvanom00_xkuzni04_xkrato61_xsvobo1x/repo/install
	rm -rf ../../xvanom00_xkuzni04_xkrato61_xsvobo1x/repo/doc
	mkdir -p ../../xvanom00_xkuzni04_xkrato61_xsvobo1x/repo
	mkdir ../../xvanom00_xkuzni04_xkrato61_xsvobo1x/install
	mkdir ../../xvanom00_xkuzni04_xkrato61_xsvobo1x/doc
	cp -a ../../S_posters_VUT_IVS_team_project/. ../../xvanom00_xkuzni04_xkrato61_xsvobo1x/repo/
	cp -a ../doc/. ../../xvanom00_xkuzni04_xkrato61_xsvobo1x/doc/
	cp -a ../slothcalc.deb ../../xvanom00_xkuzni04_xkrato61_xsvobo1x/install/
	cp -a ../dokumentace.pdf ../../xvanom00_xkuzni04_xkrato61_xsvobo1x/install/

clean:
	rm -rf ../slothcalc/usr/bin/
	rm -rf ./build/
	rm -rf ./dist/
	rm -rf ./*.spec
	rm -rf ../*.deb
	cd .. && rm -rf doc
