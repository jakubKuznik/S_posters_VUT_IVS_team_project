from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from gui import *

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <title>MathJax v3 with interactive TeX input and HTML output</title>
  <script type="text/javascript" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">

    MathJax.Hub.Config({
    jax: ["input/TeX","output/HTML-CSS"],
    displayAlign: "left"

  </script>


  <script>
    function convert(input) {
      output = document.getElementById('output');
      output.innerHTML = '';
      MathJax.texReset();
      var options = MathJax.getMetricsFor(output);
      options.display = true;
      MathJax.tex2chtmlPromise(input, options).then(function (node) {
        output.appendChild(node);
        MathJax.startup.document.clear();
        MathJax.startup.document.updateDocument();
      }).catch(function (err) {
        output.appendChild(document.createTextNode(err.message));
      });
    }
  </script>
  <style>
  body, html {
    padding: 0;
    margin: 0;
  }
  #output {
    font-size: 120%;
    min-height: 2em;
    padding: 0;
    margin: 0;
  }
  .left {
    float: left;
  }
  .right {
    float: right;
  }
  </style>
</head>
<body>
<div id="output" class="left"></div>
</body>
</html>
"""


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui = Ui_s_cals()
        ui.setupUi(self)
        self.ui = ui
        ui.view.setHtml(html)
        page = ui.view.page()
        page.loadFinished.connect(self.onLoadFinished)
        ui.edit.setText("")
        ui.edit.textChanged.connect(self.onTextChanged)
        self._ready = False

    def onLoadFinished(self):
        if self._ready:
            return
        self._ready = True
        self.onTextChanged(self.ui.edit.text())

    def onTextChanged(self, text):
        text = text.replace("\\", "\\\\")  # To escape special characters
        page = self.ui.view.page()
        page.runJavaScript('convert("{}");'.format(text))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    app.exec()
