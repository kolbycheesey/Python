
# https://github.com/jmcgeheeiv/pyqttestexample/blob/master/src/MargaritaMixerTest.py#L70
# https://doc.qt.io/qt-6/qttest-index.html
import pytest

from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtGui import QFont
#from PyQt6.QtTest import 

import example_app

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.text_label = QLabel()
        self.text_label.setText("Hello World!")
        self.text_label.setFont(QFont('Arial', 20))
        
        self.text_label1 = QLabel()
        self.text_label1.setText("New World!")
        self.text_label1.setFont(QFont('Arial', 20))

        self.button = QPushButton("Fancy Button")
        self.button.setFont(QFont('Arial', 14))
        self.button.clicked.connect(lambda: self.text_label.setText("Changed!"))
        
        self.button1 = QPushButton("Fancy Button1")
        self.button1.setFont(QFont('Arial', 14))
        self.button1.clicked.connect(lambda: self.text_label1.setText("Changed again!"))

        self.setGeometry(50, 50, 300, 200)
        self.setWindowTitle("PyQt6 Example")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text_label)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text_label1)
        self.layout.addWidget(self.button1)
        self.setLayout(self.layout)


@pytest.fixture
def app(qtbot):
    test_hello_app = MyApp()

    return test_hello_app


def test_label(app):
    assert app.text_label.text() == "Hello World!"


def test_label_after_click(app, qtbot):
    assert(isinstance(app, QWidget))
    qtbot.mouseClick(app, QtCore.Qt.MouseButton.LeftButton)
    assert app.text_label.text() == "Changed!"
