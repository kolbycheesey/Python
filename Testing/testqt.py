# import numpy as np
# import pyqtgraph as pg
# from PyQt6 import QtGui, QtCore
# from PyQt6.QtWidgets import QDockWidget, QWidget, QMainWindow, QApplication
# import PyQt6

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__




#         image=np.eye(3)
#         print(image)
        
#         a = [[1, 2, 3], [4, 5, 6]]
#         nd_a = np.array(a)
        
#         #b = [[0,1],[1,1],[1,2],[0,2],[2,1]]
#         b = [[26,26], [0,0]]
#         nd_b = np.array(b)
#         print(nd_b)
        
#         c = [0,1,2,3,4,5]
#         nd_c = np.array(c)

#         plot1 = pg.PlotItem()
#         #plot1._in
#         img = pg.ImageItem( nd_b, levels=(0,1) ) #levels=(0,1)
#         #img.maptoData()
#         #img._in
#         #tr = QtGui.QTransform()  # prepare ImageItem transformation:
#         #tr.scale(6.0, 3.0)       # scale horizontal and vertical axes
#         #tr.translate(-1.5, -1.5) # move 3x3 image to locate center at axis origin
#         #img.setTransform(tr)
#         plot1.addItem( img )  # add ImageItem to PlotItem
#         plot1.showAxes(True)  # frame it with a full set of axes
#         #plot1.invertY(True)   # vertical axis counts top to bottom
#         print(plot1)
#         self.main = QMainWindow()
#         #win = pg.GraphicsView()
#         win = pg.PlotWidget(plotItem=plot1)
#         #win = pg.GraphicsLayoutWidget()
#         #win.addPlot(plot1)
#         #win.setCentralItem(img)
#         #win.show()
#         #widget = pg.PlotWidget()
#         #widget.addItem(img)
#         #main = QDockWidget("Testing Window")
#         #popwidget = QWidget()
#         #popwidget.setLayou
#         self.main.setCentralWidget(win)
#         self.main.show()
        
#         """
#         roiHitbox = self.roi.mapRectToItem(self.dataPlot, self.roi.boundingRect())
#         points = self.dataPlot.points()
#         collidedPoints = []
#         for p in points:
#             #p.viewPos() is a QPointF.
#             if(roiHitbox.contains(p.viewPos())):
#                 collidedPoints.append(p)
#         newList = set(collidedPoints)   
#         """
        
#         #https://stackoverflow.com/questions/75689465/pyqtgraph-get-spotitem-objects-within-roi-selection
#         #https://pyqtgraph.readthedocs.io/en/latest/_modules/pyqtgraph/graphicsItems/ROI.html#RectROI   -> Look at shape and QPainterPath
#         #https://stackoverflow.com/questions/76574722/pytest-qt-to-test-menu-functionality
        
# if __name__ == '__main__':

#     import sys 
#     app = QApplication(sys.argv)
#     window = Window()
#     sys.exit(app.exec())


import sys
import matplotlib
import secrets

matplotlib.use('QtAgg')

from PyQt6 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        toolbar = NavigationToolbar2QT(self.canvas, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [secrets.SystemRandom().randint(0, 10) for i in range(n_data)]
        self.update_plot()

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:] + [secrets.SystemRandom().randint(0, 10)]
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec()
