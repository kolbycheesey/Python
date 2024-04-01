import pytest
import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import QLabel, QMainWindow, QWidget, QApplication
from example_app import MyApp


def test_hello(qtbot):
    # widget = HelloWidget()
    app = QApplication(sys.argv)
    widget = app
    qtbot.addWidget(widget)

    # click in the Greet button and make sure it updates the appropriate label
    qtbot.mouseClick(widget.button, QtCore.Qt.MouseButton.LeftButton)

    # assert widget.greet_label.text() == "Hello!"
    assert widget.text_label.text() == "Hello!"
