import sys
import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QMainWindow
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi("test.ui", self)

        scene = QGraphicsScene()
        self.graphicsView.setScene(scene)

        self.plotWdgt = pg.PlotWidget()
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        plot_item = self.plotWdgt.plot(data)

        proxy_widget = scene.addWidget(self.plotWdgt)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()