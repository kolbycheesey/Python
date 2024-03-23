from PyQt6.QtWidgets import *
import sys
import numpy as np
import pyqtgraph as pg
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from collections import namedtuple
 
 
 
# Main window class
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
        
        self.imv = None
        self.img = None
        
 
        # setting title
        self.setWindowTitle("PyQtGraph")
 
        # setting geometry
        self.setGeometry(100, 100, 600, 500)
 
        # icon
        icon = QIcon("skin.png")
 
        # setting icon to the window
        self.setWindowIcon(icon)
 
        # calling method
        self.UiComponents()
        
        self.imv.roi.sigRegionChanged.connect(self.function)
 
        # showing all the widgets
        self.show()
 
    # method for components
    def UiComponents(self):
 
        # creating a widget object
        widget = QWidget()
 
        # creating a label
        label = QLabel("Geeksforgeeks Image View")
 
        # setting minimum width
        label.setMinimumWidth(130)
 
        # making label do word wrap
        label.setWordWrap(True)
 
        # setting configuration options
        pg.setConfigOptions(antialias=True)
 
        # creating image view object
        imv = pg.ImageView()
        """print("Before")
        print("\n\n")
        print(imv.image)
        print("\n\n")
        print("After")"""
 
        # Create random 3D data set with noisy signals
        #img = pg.gaussianFilter(np.random.normal(size=(200, 200)), (5, 5)) * 20 + 100
 
        # setting new axis to image
        #img = img[np.newaxis, :, :]
 
        # decay data
        #decay = np.exp(-np.linspace(0, 0.3, 100))[:, np.newaxis, np.newaxis]
 
        # random data
        data = np.random.normal(size=(100, 100, 1))
        print(data.shape)
        #data += img * decay
        #data += 2
 
        # adding time-varying signal
        #sig = np.zeros(data.shape[0])
        #sig[30:] += np.exp(-np.linspace(1, 10, 70))
        #sig[40:] += np.exp(-np.linspace(1, 10, 60))
        #sig[70:] += np.exp(-np.linspace(1, 10, 30))
 
        #sig = sig[:, np.newaxis, np.newaxis] * 3
        #data[:, 50:60, 30:40] += sig
        
        
        """print("Before")
        print("\n\n")
        print(imv.image)
        print("\n\n")
        print("After")"""
 
        # Displaying the data and assign each frame a time value from 1.0 to 3.0
        imv.setImage(data, xvals=np.linspace(1., 3., data.shape[0])) #-> imv.image which then gets processed and normed in getprocessedimage -> and imageItem is just an ImageItem() class
        print(f"xvals = {np.linspace(1., 3., data.shape[0])}")
        print(data.shape[0])
        print(data)
        #imv.setImage(img, xvals=np.linspace(1., 3., data.shape[0]))
        
        """print("Before")
        print("\n\n")
        print(imv.image)
        print("\n\n")
        print("After")"""
 
        # Set a custom color map
        colors = [
            (0, 0, 0),
            (45, 5, 61),
            (84, 42, 55),
            (150, 87, 60),
            (208, 171, 141),
            (255, 255, 255)
        ]
 
        # color map
        cmap = pg.ColorMap(pos=np.linspace(0.0, 1.0, 6), color=colors)
 
        # setting color map to the image view
        imv.setColorMap(cmap)
 
        # Creating a grid layout
        layout = QGridLayout()
 
        # minimum width value of the label
        label.setFixedWidth(130)
 
        # setting this layout to the widget
        widget.setLayout(layout)
 
        # adding label in the layout
        layout.addWidget(label, 1, 0)
 
        # plot window goes on right side, spanning 3 rows
        layout.addWidget(imv, 0, 1, 3, 1)
 
        # setting this widget as central widget of the main window
        self.setCentralWidget(widget)
        self.imv = imv
        #self.img = img
        
        #imv.roi.clicked.connect(self.function)
        
        
    def function(self):
        #self.imv.roi.getArrayRegion()
        image = self.imv.getProcessedImage()
        if image.ndim == 2:
            axes = (0, 1)
        elif image.ndim == 3:
            axes = (1, 2)
        else:
            return
        
        data, coords = self.imv.roi.getArrayRegion(image.view(np.ndarray), self.imv.imageItem, axes, returnMappedCoords=True)
        print(f"data: {data}")
        print(f"coords: {coords}")
 
 
         
# Driver Code
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())