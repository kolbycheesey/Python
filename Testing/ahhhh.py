from PyQt6.QtWidgets import * 
from PyQt6 import QtCore, QtGui 
from PyQt6.QtGui import * 
from PyQt6.QtCore import * 
import sys 
  
  
class Window(QMainWindow): 
  
    def __init__(self): 
        super().__init__() 
  
        # setting title 
        self.setWindowTitle("Python ") 
  
        # setting geometry 
        self.setGeometry(100, 100, 600, 400) 
  
        # calling method 
        self.UiComponents() 
  
        # showing all the widgets 
        self.show() 
  
    # method for widgets 
    def UiComponents(self): 
        # creating progress bar 
        bar1 = QProgressBar(self) 
  
        # setting geometry to progress bar 
        bar1.setGeometry(200, 100, 200, 30) 
  
        # setting the value 
        bar1.setValue(70) 
  
        # setting alignment to center 
        bar1.setAlignment(Qt.AlignmentFlag.AlignCenter) 
  
        # setting font and the size 
        bar1.setFont(QFont('Arial', 15)) 
  
        # creating progress bar 
        bar2 = QProgressBar(self) 
  
        # setting geometry to progress bar 
        bar2.setGeometry(200, 200, 200, 30) 
  
        # setting the value 
        bar2.setValue(100) 
  
        # adding text using setFormat 
        bar2.setFormat("Hello Geeks") 
  
        # setting alignment to center 
        bar2.setAlignment(Qt.AlignmentFlag.AlignCenter) 
  
        # setting font and the size 
        bar2.setFont(QFont('Times', 7))
        
        bar2.setStyleSheet("QProgressBar::chunk {background-color: red}")
  
  
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
  
# start the app 
sys.exit(App.exec()) 