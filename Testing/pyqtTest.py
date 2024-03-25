import sys
import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QMainWindow
from PyQt6 import uic
from PyQt6.QtWidgets import *
import sys
import numpy as np
import pyqtgraph as pg
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from ImageViewTemplate import Ui_Form
#from collections import namedtuple


class MainWindow(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi("test.ui", self)

        scene = QGraphicsScene()
        self.graphicsView.setScene(scene)

        self.plotWdgt = pg.PlotWidget()
        self.ImageWdgt = pg.ImageItem()
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        plot_item = self.plotWdgt.plot(data)

        proxy_widget1 = scene.addWidget(self.plotWdgt)
        #proxy_widget2 = scene.addItem(self.ImageWdgt)
        
        scene.sigRangeChanged.connect(self.function)
        
        """
        self.levelMax = 4096
        self.levelMin = 0
        self.name = "ImageView"
        self.image = None
        self.imageDisp = None
        #self.ui = Ui_Form()
        #self.ui.setupUi(self)
        #self.scene = self.ui.graphicsView.sceneObj
        
        self.imageItem = pg.ImageItem()
        self.scene.addItem(self.imageItem, 0, 0)"""

    def function(self):
        print("When do we move")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()