import numpy as np
import pyqtgraph as pg
from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QDockWidget, QWidget, QMainWindow, QApplication
import PyQt6

class Window(QMainWindow):
    def __init__(self):
        super().__init__




        image=np.eye(3)
        print(image)
        
        a = [[1, 2, 3], [4, 5, 6]]
        nd_a = np.array(a)
        
        #b = [[0,1],[1,1],[1,2],[0,2],[2,1]]
        b = [[26,26], [0,0]]
        nd_b = np.array(b)
        print(nd_b)
        
        c = [0,1,2,3,4,5]
        nd_c = np.array(c)

        plot1 = pg.PlotItem()
        #plot1._in
        img = pg.ImageItem( nd_b, levels=(0,1) ) #levels=(0,1)
        #img.maptoData()
        #img._in
        #tr = QtGui.QTransform()  # prepare ImageItem transformation:
        #tr.scale(6.0, 3.0)       # scale horizontal and vertical axes
        #tr.translate(-1.5, -1.5) # move 3x3 image to locate center at axis origin
        #img.setTransform(tr)
        plot1.addItem( img )  # add ImageItem to PlotItem
        plot1.showAxes(True)  # frame it with a full set of axes
        #plot1.invertY(True)   # vertical axis counts top to bottom
        print(plot1)
        self.main = QMainWindow()
        #win = pg.GraphicsView()
        win = pg.PlotWidget(plotItem=plot1)
        #win = pg.GraphicsLayoutWidget()
        #win.addPlot(plot1)
        #win.setCentralItem(img)
        #win.show()
        #widget = pg.PlotWidget()
        #widget.addItem(img)
        #main = QDockWidget("Testing Window")
        #popwidget = QWidget()
        #popwidget.setLayou
        self.main.setCentralWidget(win)
        self.main.show()
        
        """
        roiHitbox = self.roi.mapRectToItem(self.dataPlot, self.roi.boundingRect())
        points = self.dataPlot.points()
        collidedPoints = []
        for p in points:
            #p.viewPos() is a QPointF.
            if(roiHitbox.contains(p.viewPos())):
                collidedPoints.append(p)
        newList = set(collidedPoints)   
        """
        
        #https://stackoverflow.com/questions/75689465/pyqtgraph-get-spotitem-objects-within-roi-selection
        
if __name__ == '__main__':

    import sys 
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())