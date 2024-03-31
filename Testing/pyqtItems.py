import sys

from PyQt6.QtWidgets import * 
from PyQt6 import QtCore, QtGui 
from PyQt6.QtGui import * 
from PyQt6.QtCore import * 

#from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")
        
        prog = QProgressBar()
        # prog.text("Random Bar")
        # prog.setRange(0,1)
        # prog.setProperty(name="Button 1")
        # prog.setProperty('name: Button1')
        # prog.setTextVisible(False)
        #prog.setStyleSheet("QProgressBar::chunk {background-color: red;}")
        prog.setFormat("Button1")
        prog.setAlignment(Qt.AlignmentFlag.AlignCenter)
        prog.setFont(QFont('Arial', 15))
        prog.setValue(100)
        string = prog.styleSheet()
        print (string)
        
        #newprog = QRadioButton()
        
        #newprog = QProgressBar()
        #prog.text("Random Bar")
        #newprog.setRange(0,1)
        #prog.setProperty(name="Button 1")
        #prog.setProperty('name: Button1')
        #newprog.setTextVisible(False)
        #prog.setStyleSheet("QProgressBar::chunk {background-color: red;}")
        #newprog.setFormat("Button1")
        #newprog.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #newprog.setFont(QFont('Arial', 15))
        #newprog.setValue(100)
        
        # le = QLineEdit()
        # le.setText("Hello")
        # name = QLabel()
        # name.

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QPushButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())
            
        layout.addWidget(prog)
        #layout.addWidget(newprog)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
