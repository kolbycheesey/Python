import sys

from PyQt6.QtWidgets import * 
from PyQt6 import QtCore, QtGui 
from PyQt6.QtGui import * 
from PyQt6.QtCore import * 

#from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QProgressBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")
        
        prog = QProgressBar()
        prog.setRange(0,1)
        prog.setTextVisible(False)
        prog.setGeometry(200, 100, 200, 30)
        #prog.setStyleSheet("QProgressBar::chunk {background-color: red;}")
        prog.setFormat("Button1")
        prog.setAlignment(Qt.AlignmentFlag.AlignCenter)
        prog.setFont(QFont('Arial', 15))
        prog.setValue(1)
        
        self.setCentralWidget(prog)
        self.show()
        
        
app = QApplication(sys.argv)
window = MainWindow()
#window.show()

app.exec()