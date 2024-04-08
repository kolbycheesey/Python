import sys
import matplotlib
matplotlib.use('QtAgg')

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QVBoxLayout, QRadioButton
from PyQt6.QtGui import QPixmap, QPainter, QColor

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, 
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

from rectangle import Rectangle


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.setCentralWidget(sc)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        #toolbar = NavigationToolbar(sc, self)
        #toolbar = CustomToolbar(self, sc)       ##This needs to move down below vbox layout

    ##  CustomToolbar needs to be added after the graph

        layout = QtWidgets.QVBoxLayout()

        toolbar = CustomToolbar(self,sc)
        layout.addWidget(toolbar)
        layout.addWidget(sc)
        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

class CustomToolbar(NavigationToolbar):
    def __init__(self, canvas, parent=None):
        super(CustomToolbar, self).__init__(parent)
        
        self.rect = Rectangle()
        self.gate_type_radio = QRadioButton("Rectangle", self)
        self.gate_type_radio.setChecked(False)
        self.gate_type_radio.toggled.connect(lambda:self.btnstate(self.gate_type_radio))
        self.addWidget(self.gate_type_radio)

    def btnstate(self,b):
        if b.isChecked() == True:
            print("Button is pressed!") ##-> run rectangle option
            self.rect.paintEvent(True)
        else:
            print("Button is not pressed!!!")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec()