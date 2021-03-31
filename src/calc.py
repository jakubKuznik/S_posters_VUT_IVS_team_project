from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from gui import *


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui = Ui_s_cals()
        ui.setupUi(self)
        self.ui = ui
        ui.view.setHtml(self.open_html_template())
        page = ui.view.page()
        page.loadFinished.connect(self.onLoadFinished)
        ui.edit.setText("")
        ui.edit.textChanged.connect(self.onTextChanged)
        self.ready = False

    def onLoadFinished(self):
        if self.ready:
            return
        self.ready = True
        self.onTextChanged(self.ui.edit.text())

    def onTextChanged(self, text):
        text = text.replace("\\", "\\\\")  # To escape special characters
        page = self.ui.view.page()
        page.runJavaScript('convert("{}");'.format(text))

    @staticmethod
    def open_html_template():
        with open('template.html') as f:
            return ''.join(f.readlines())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    app.exec()
