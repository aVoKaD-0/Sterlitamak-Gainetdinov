import sys
import random
from PyQt6 import QtWidgets, QtGui, QtCore

class UI:
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 500, 100, 30))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslate_ui(MainWindow)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Форма с окружностями"))
        self.pushButton.setText(_translate("MainWindow", "Добавить окружность"))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = UI()
        self.ui.setup_ui(self)
        self.button = self.ui.pushButton
        self.button.clicked.connect(self.add_circle)
        self.circles = []
        self.widget = self.ui.centralwidget
        self.widget.paintEvent = self.paint_event

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.widget.width() - diameter)
        y = random.randint(0, self.widget.height() - diameter)
        color = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.widget.update()

    def paint_event(self, event):
        painter = QtGui.QPainter(self.widget)
        for circle in self.circles:
            x, y, diameter, color = circle
            painter.setPen(QtGui.QPen(color))
            painter.setBrush(QtGui.QBrush(color))
            painter.drawEllipse(x, y, diameter, diameter)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main() 