mkdir -p ../installer/usr/share/impcalc 2>/dev/null
cp  math_lib.py ../installer/usr/share/impcalc/math_lib.py
cp  gui.py ../installer/usr/share/impcalc/gui.py
cp  calc.py ../installer/usr/share/impcalc/calc.py && chmod +x ../installer/usr/share/impcalc/calc.py
mkdir -p ../installer/usr/local/bin 2>/dev/null
ln -sf /usr/share/impcalc/calc.py ../installer/usr/local/bin/impcalc-calculator
mkdir ../installer/tmp 2>/dev/null
cp requirements.txt ../installer/tmp/requirements.txt
chmod +x ../installer/DEBIAN/postinst
dpkg-deb --build ../installer/ ../installer/installer.deb