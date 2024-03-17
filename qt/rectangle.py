import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt, QPoint, QRect
from PyQt6.QtGui import QPixmap, QPainter, QColor



class Rectangle(QWidget):
	def __init__(self, parent=None):#, _button):
		super().__init__()
		##self.window_width, self.window_height = 1200, 800
		##self.setMinimumSize(self.window_width, self.window_height)

		##layout = QVBoxLayout()
		##self.setLayout(layout)

		self.pix = QPixmap(self.rect().size()) ##does this need to be changed to what the graph size is?
		##self.pix.fill(2147483647) #INT_MAX
		print(f"Lets see the size: {self.rect().size()}")

		self.begin, self.destination = QPoint(), QPoint()	

    #Need to change the event.buttons option or ad that it checks the radio button
	#Do I need to update the button in histogram and just set the variable in the
	#class declaration???

	def paintEvent(self, event):
		print("event1")
		painter = QPainter(self)
		painter.drawPixmap(QPoint(), self.pix)

		if not self.begin.isNull() and not self.destination.isNull():
			rect = QRect(self.begin, self.destination)
			painter.drawRect(rect.normalized())

	def mousePressEvent(self, event):
		if event.buttons() & Qt.MouseButton.LeftButton:
			print('Point 1')
			self.begin = event.pos()
			self.destination = self.begin
			self.update()

	def mouseMoveEvent(self, event):
		if event.buttons() & Qt.MouseButton.LeftButton:		
			print('Point 2')	
			self.destination = event.pos()
			self.update()

	def mouseReleaseEvent(self, event):
		print('Point 3')
		if event.buttons() & Qt.MouseButton.LeftButton:
			rect = QRect(self.begin, self.destination)
			painter = QPainter(self.pix)
			painter.drawRect(rect.normalized())

			self.begin, self.destination = QPoint(), QPoint()
			self.update()

if __name__ == '__main__':
	# don't auto scale when drag app to a different monitor.
	# QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
	
	app = QApplication(sys.argv)
	app.setStyleSheet('''
		QWidget {
			font-size: 30px;
		}
	''')
	
	myApp = Rectangle()
	myApp.show()

	try:
		sys.exit(app.exec())
	except SystemExit:
		print('Closing Window...')

