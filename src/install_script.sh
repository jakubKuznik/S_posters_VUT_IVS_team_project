mkdir -p ../installer/usr/share/slothcalc 2>/dev/null

cp math_lib.py ../installer/usr/share/slothcalc/math_lib.py
cp gui.py ../installer/usr/share/slothcalc/gui.py
cp calc_parser.py ../installer/usr/share/slothcalc/calc_parser.py
cp help_form.html ../installer/usr/share/slothcalc/help_form.html
cp calc.py ../installer/usr/share/slothcalc/calc.py && chmod +x ../installer/usr/share/slothcalc/calc.py
cp standard_deviation.py ../installer/usr/share/slothcalc/standard_deviation.py
cp icon.png ../installer/usr/share/slothcalc/icon.png

cp bulb_on.png ../installer/usr/share/slothcalc/bulb_on.png
cp bulb_off.png ../installer/usr/share/slothcalc/bulb_off.png

cp question_on.png ../installer/usr/share/slothcalc/question_on.png
cp question_off.png ../installer/usr/share/slothcalc/question_off.png




mkdir -p ../installer/usr/local/bin 2>/dev/null
ln -sf /usr/share/slothcalc/calc.py ../installer/usr/local/bin/slothcalc-calculator
mkdir ../installer/tmp 2>/dev/null
cp requirements.txt ../installer/tmp/requirements.txt
chmod +x ../installer/DEBIAN/postinst
dpkg-deb --build ../installer/ ../installer/sloth_install.deb