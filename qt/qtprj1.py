#hello.py
"""base program with PyQt6"""

import sys
from functools import partial
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, 
    #QHBoxLayout,
    #QVBoxLayout,
    QGridLayout,
    QPushButton,
    #QLabel,
    #QFormLayout,
    QLineEdit,
    #QDialog,
    #QDialogButtonBox, 
    QVBoxLayout,
    QWidget,
    QMainWindow
    #QStatusBar,
    #QToolBar
)

#app = QApplication([])
#window = QWidget()
#window.setWindowTitle("Hello World App")
#window.setGeometry(100,100,280,80)      ##x,y,width,height
#helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
#helloMsg.move(60,15)

#window.setWindowTitle("QHBoxLayout")
#layout = QHBoxLayout()
#layout.addWidget(QPushButton("Left"))
#layout.addWidget(QPushButton("Center"))
#layout.addWidget(QPushButton("Right"))
#window.setLayout(layout)

#window.setWindowTitle("QVBoxLayout")
#layout = QVBoxLayout()
#layout.addWidget(QPushButton("Top"))
#layout.addWidget(QPushButton("Center"))
#layout.addWidget(QPushButton("Bottom"))
#window.setLayout(layout)

#window.setWindowTitle("QGridLayout")
#layout = QGridLayout()
#layout.addWidget(QPushButton("Button (0, 0)"), 0, 0)
#layout.addWidget(QPushButton("Button (0, 1)"), 0, 1)
#layout.addWidget(QPushButton("Button (0, 2)"), 0, 2)
#layout.addWidget(QPushButton("Button (1, 0)"), 1, 0)
#layout.addWidget(QPushButton("Button (1, 1)"), 1, 1)
#layout.addWidget(QPushButton("Button (1, 2)"), 1, 2)
#layout.addWidget(QPushButton("Button (2, 0)"), 2, 0)
#layout.addWidget(QPushButton("Button (2, 1) + 2 Columns Span"), 2, 1, 1, 2)
#window.setLayout(layout)

#layout = QFormLayout()
#layout.addRow("Name:", QLineEdit())
#layout.addRow("Age:", QLineEdit())
#layout.addRow("Job:", QLineEdit())
#layout.addRow("Hobbies:", QLineEdit())
#window.setLayout(layout)

#window.show()
#sys.exit(app.exec())

'''
class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Window Title")
        dialogLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Age:", QLineEdit())
        formLayout.addRow("Job:", QLineEdit())
        formLayout.addRow("Hobbies:", QLineEdit())
        dialogLayout.addLayout(formLayout)
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel | 
            QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)
'''        
        
        
#class Window(QMainWindow):
#    def __init__(self):
#        super().__init__(parent=None)
#        self.setWindowTitle("QMainWindow")
#        self.setCentralWidget(QLabel("I'm the Central Widget"))
#        self._createMenu()
#        self._createToolBar()
#        self._createStatusBar()

#    def _createMenu(self):
#        menu = self.menuBar().addMenu("&Menu")
#        menu.addAction("&Exit", self.close)

#    def _createToolBar(self):
#        tools = QToolBar()
#        tools.addAction("Exit", self.close)
#        self.addToolBar(tools)

#    def _createStatusBar(self):
#        status = QStatusBar()
#        status.showMessage("I'm the Status Bar")
#        self.setStatusBar(status)


#if __name__ == "__main__":
#    app = QApplication([])
#    window = Window()
#    window.show()
#    sys.exit(app.exec())

'''
name ="World!"
def greet():
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText(f"Hello, {name}")


app = QApplication([])
window = QWidget()
window.setWindowTitle("Signals and slots")
layout = QVBoxLayout()

button = QPushButton("Greet")
#button.clicked.connect(partial(greet, "World!"))
button.clicked.connect(greet)

layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())
'''

ERROR_MSG = "ERR"
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40


class PyCalcWindow(QMainWindow):
    """PyCalc's main window (GUI or view)."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()
        
    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
        
    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]
        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)

        self.generalLayout.addLayout(buttonsLayout)
        
    def setDisplayText(self, text):
        """Set the display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get the display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")
        
def evaluateExpression(expression):
    """Evaluate an expression (Model)."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result

class PyCalc:
    """PyCalc's controller class."""

    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)


def main():
    """PyCalc's main function."""
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    PyCalc(model=evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcApp.exec())

if __name__ == "__main__":
    main()