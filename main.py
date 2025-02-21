import sys
import random
from PyQt6 import QtWidgets, uic, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)
        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.button.clicked.connect(self.add_circle)
        self.circles = []
        self.widget = self.findChild(QtWidgets.QWidget, 'centralwidget')
        self.widget.paintEvent = self.paint_event

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.widget.width() - diameter)
        y = random.randint(0, self.widget.height() - diameter)
        self.circles.append((x, y, diameter))
        self.widget.update()

    def paint_event(self, event):
        painter = QtGui.QPainter(self.widget)
        painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 0)))
        painter.setBrush(QtGui.QBrush(QtGui.QColor(255, 255, 0)))
        for circle in self.circles:
            x, y, diameter = circle
            painter.drawEllipse(x, y, diameter, diameter)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('Форма с окружностями')
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main() 