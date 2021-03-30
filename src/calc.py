from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from gui import *
html = """
<!DOCTYPE html>
<html lang="en">
<head>

  <title>MathJax v3 with interactive TeX input and HTML output</title>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
  <script>MathJax.Hub.Config({
    jax: ["input/TeX","output/HTML-CSS"],
    displayAlign: "left"
});
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
  .MathJax_Display { text-align : left !important; }
  }
  #output {
    font-size: 100%;
    min-height: 2em;
  }
  </style>
</head>
<body>
<div id="output"></div>
</body>
</html>
"""


class Window(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        ui = Window_Ui()
        ui.setupUi(self)
        self._ui = ui
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
        self.onTextChanged(self._ui.edit.text())

    def onTextChanged(self, text):
        text = text.replace("\\","\\\\") #To escape special characters
        print(text)
        page = self._ui.view.page()
        page.runJavaScript('convert("{}");'.format(text))



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    app.exec()
